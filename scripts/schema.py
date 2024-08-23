import json
import re
from dataclasses import dataclass, field
from keyword import iskeyword
from pathlib import Path
from typing import ClassVar, Optional, Union, cast

from markdownify import markdownify as md  # type: ignore[import-untyped]


def rst(markdown: str) -> str:
    return (
        cast(str, md(markdown))
        .replace("\\_", "_")
        .replace("\\-", "-")
        .replace("\\>", ">")
    )


project_dir = Path(__file__).resolve().parent.parent
openapi_dir = project_dir.joinpath("openapi/generated")


def gen() -> None:
    schema = json.load(open(project_dir.joinpath("openapi/v2.openapi.json")))
    generator = SchemaGenerator(
        schema,
        [
            "/payments",
            "/payment-schedules",
            "/identity-verifications",
            "/billing-keys",
            "/cash-receipts",
            "/kakaopay",
        ],
    )
    generator.generate_files()


Record = dict[str, "RecordValue"]
RecordValue = Union[str, int, float, bool, list["RecordValue"], Record]


@dataclass
class Documented:
    title: Optional[str]
    description: Optional[str]


@dataclass
class Spec(Documented):
    name: str
    as_type: str
    refs: set[str]
    properties: Optional[list["Spec"]] = None

    @classmethod
    def empty(cls, name: str) -> "Spec":
        return Spec(
            name=name,
            as_type="",
            title=None,
            description=None,
            properties=[],
            refs=set(),
        )


@dataclass
class Operation(Documented):
    name: str
    path: str
    method: str
    param: Spec
    query: Spec
    body: Optional[str]
    success: Optional[str]
    returns: Optional[str]
    error: str
    title: Optional[str]
    description: Optional[str]


@dataclass
class SchemaGenerator:
    resolved_names: set[str] = field(default_factory=set, init=False)
    operations: list[Operation] = field(default_factory=list, init=False)
    schemas: dict[str, Spec] = field(default_factory=dict, init=False)
    document: Record
    include_prefixes: list[str]
    document_schemas: Record = field(init=False)

    def __post_init__(self) -> None:
        components = self.document["components"]
        if isinstance(components, dict):
            schemas = components["schemas"]
            if isinstance(schemas, dict):
                self.document_schemas = schemas
        self.visit_document()

    @classmethod
    def parse_ref(cls, ref: str) -> str:
        return ref.rsplit("/", 1)[-1]

    def visit_document(self) -> None:
        paths = self.document["paths"]
        if isinstance(paths, dict):
            for path, entry in paths.items():
                if not any(path.startswith(prefix) for prefix in self.include_prefixes):
                    continue
                if not isinstance(entry, dict):
                    continue
                for method, schema in entry.items():
                    if not isinstance(schema, dict):
                        continue
                    operation_id = schema.get("operationId")
                    if not isinstance(operation_id, str):
                        continue
                    class_name = to_pascal_case(operation_id)
                    if not isinstance(operation_id, str):
                        continue
                    title = schema.get("x-portone-title")
                    if title is not None and not isinstance(title, str):
                        continue
                    description = schema.get("x-portone-description")
                    if description is not None and not isinstance(description, str):
                        continue
                    portone_error = schema.get("x-portone-error")
                    if not isinstance(portone_error, dict):
                        continue
                    error_ref = portone_error.get("$ref")
                    if not isinstance(error_ref, str):
                        continue
                    error = self.parse_ref(error_ref)
                    self.export_type(error)
                    request_body = schema.get("requestBody")
                    body = None
                    if isinstance(request_body, dict):
                        content = request_body.get("content")
                        if isinstance(content, dict):
                            json = content.get("application/json")
                            if isinstance(json, dict):
                                body_schema = json.get("schema")
                                if isinstance(body_schema, dict):
                                    body_ref = body_schema.get("$ref")
                                    if isinstance(body_ref, str):
                                        body = self.parse_ref(body_ref)
                                        self.export_type(body)
                    parameters_schema = schema.get("parameters")
                    param = []
                    query = []
                    if isinstance(parameters_schema, list):
                        for parameter in parameters_schema:
                            if not isinstance(parameter, dict):
                                continue
                            name = parameter["name"]
                            if not isinstance(name, str):
                                continue
                            if name == "requestBody":
                                continue
                            where = parameter["in"]
                            if not isinstance(where, str):
                                continue
                            parameter_schema = parameter["schema"]
                            if not isinstance(parameter_schema, dict):
                                continue
                            parameter_description = parameter.get("description")
                            if parameter_description is not None and not isinstance(
                                parameter_description, str
                            ):
                                continue
                            spec = self.visit_schema(parameter_schema, name)
                            spec.description = parameter_description
                            if where == "path":
                                param.append(spec)
                            elif where == "query":
                                required = parameter.get("required", False)
                                if not isinstance(required, bool):
                                    continue
                                if not required:
                                    spec.as_type = f"Optional[{spec.as_type}]"
                                    spec.refs.add("Optional")
                                query.append(spec)
                    response = schema.get("responses")
                    success = None
                    returns = None
                    if isinstance(response, dict):
                        ok = response["200"]
                        if isinstance(ok, dict):
                            ok_desc = ok.get("description")
                            if isinstance(ok_desc, str):
                                returns = ok_desc
                            content = ok.get("content")
                            if isinstance(content, dict):
                                json = content.get("application/json")
                                if isinstance(json, dict):
                                    success_schema = json.get("schema")
                                    if isinstance(success_schema, dict):
                                        success_ref = success_schema.get("$ref")
                                        if isinstance(success_ref, str):
                                            success = self.parse_ref(success_ref)
                                            self.export_type(success)
                    self.operations.append(
                        Operation(
                            name=operation_id,
                            path=path,
                            method=method,
                            param=Spec(
                                name=f"{class_name}Param",
                                as_type="",
                                title=None,
                                description=None,
                                properties=param,
                                refs=set(),
                            ),
                            query=Spec(
                                name=f"{class_name}Query",
                                as_type="",
                                title=None,
                                description=None,
                                properties=query,
                                refs=set(),
                            ),
                            body=body,
                            success=success,
                            error=error,
                            title=title,
                            description=description,
                            returns=returns,
                        )
                    )

    def visit_schema(self, schema: Record, name: str) -> Spec:
        title = schema.get("title")
        description = schema.get("description")
        if title is not None and not isinstance(title, str):
            raise ValueError("Invalid title value", schema, name)
        if description is not None and not isinstance(description, str):
            raise ValueError("Invalid description value", schema, name)
        ref = schema.get("$ref")
        if isinstance(ref, str):
            as_type = self.parse_ref(ref)
            self.export_type(as_type)
            return Spec(
                name=name,
                as_type=as_type,
                title=title,
                description=description,
                refs=set([as_type]),
            )
        discriminator = schema.get("discriminator")
        if isinstance(discriminator, dict):
            property_name = discriminator["propertyName"]
            mapping = discriminator["mapping"]
            if isinstance(property_name, str) and isinstance(mapping, dict):
                refs = set()
                as_types = []
                for key, ref in mapping.items():
                    if not isinstance(ref, str):
                        continue
                    name = self.parse_ref(ref)
                    self.export_type(name)
                    refs.add(name)
                    as_types.append(name)
                    spec = self.schemas[name]
                    properties = spec.properties
                    if properties is None:
                        raise ValueError(
                            f"discriminant type mismatch: {name} - {schema}"
                        )
                    for prop in properties:
                        if prop.name == property_name:
                            prop.as_type = f'Literal["{key}"]'
                            spec.refs.add("Literal")
                as_type = f"Union[{', '.join(as_types)}]"
                refs.add("Union")
                return Spec(
                    name=name,
                    as_type=as_type,
                    title=title,
                    description=description,
                    refs=refs,
                )
        type = schema.get("type")
        if isinstance(type, str):
            if type == "object":
                as_type = name
                properties = []
                raw_required = schema.get("required", [])
                if not isinstance(raw_required, list):
                    raise NotImplementedError(
                        "Unimplemented required field", schema, name
                    )
                required = set(raw_required)
                raw_properties = schema.get("properties")
                refs = set()
                if isinstance(raw_properties, dict):
                    for key, value in raw_properties.items():
                        if isinstance(value, dict):
                            spec = self.visit_schema(value, key)
                            refs.update(spec.refs)
                            if key not in required:
                                spec.as_type = f"Optional[{spec.as_type}]"
                                refs.add("Optional")
                            properties.append(spec)
                else:
                    as_type = "Any"
                    refs.add("Any")
                return Spec(
                    name=name,
                    as_type=as_type,
                    title=title,
                    description=description,
                    properties=properties,
                    refs=refs,
                )
            elif type == "array":
                items = schema.get("items")
                if isinstance(items, dict):
                    spec = self.visit_schema(items, name)
                    as_type = f"list[{spec.as_type}]"
                    return Spec(
                        name=name,
                        as_type=as_type,
                        title=title,
                        description=description,
                        refs=spec.refs,
                    )
                else:
                    raise NotImplementedError(items)
            elif type == "string":
                enum = schema.get("enum")
                if isinstance(enum, list):
                    as_type = (
                        "Literal["
                        + ", ".join(
                            [
                                f'"{literal}"'
                                for literal in enum
                                if isinstance(literal, str)
                            ]
                        )
                        + "]"
                    )
                    refs = set(["Literal"])
                else:
                    as_type = "str"
                    refs = set()
                return Spec(
                    name=name,
                    as_type=as_type,
                    title=title,
                    description=description,
                    refs=refs,
                )
            elif type == "integer":
                return Spec(
                    name=name,
                    as_type="int",
                    title=title,
                    description=description,
                    refs=set(),
                )
            elif type == "number":
                return Spec(
                    name=name,
                    as_type="float",
                    title=title,
                    description=description,
                    refs=set(),
                )
            elif type == "boolean":
                return Spec(
                    name=name,
                    as_type="bool",
                    title=title,
                    description=description,
                    refs=set(),
                )
        raise NotImplementedError(schema, name)

    def export_type(self, name: str) -> None:
        if name in self.resolved_names:
            return
        self.resolved_names.add(name)
        schema = self.document_schemas[name]
        if isinstance(schema, dict):
            self.schemas[name] = self.visit_schema(schema, name)

    def generate_files(self) -> None:
        self.generate_files_schemas(openapi_dir)
        self.generate_files_api(openapi_dir)
        openapi_dir.joinpath("__init__.py").touch()

    @classmethod
    def make_doc_lines_raw(cls, spec: Documented) -> list[str]:
        lines = []
        if spec.title:
            lines.append(spec.title)
        if spec.description:
            first = bool(lines)
            for line in rst(spec.description).strip().splitlines():
                line = line.strip()
                if first:
                    if line == "" or line == lines[-1]:
                        continue
                    lines.append("")
                    first = False
                lines.append(line)
        return lines

    @classmethod
    def make_doc_lines(cls, spec: Documented) -> list[str]:
        lines = cls.make_doc_lines_raw(spec)
        if lines:
            lines[0] = f'"""{lines[0]}'
            if len(lines) > 1:
                lines.append('"""')
            else:
                lines[-1] = f'{lines[-1]}"""'
        return lines

    def has_union(self, spec: Spec) -> bool:
        if spec.refs:
            for prop in spec.refs:
                schema = self.schemas.get(prop)
                if schema is not None and "Union" in schema.refs:
                    return True
        return False

    def generate_schema(self, spec: Spec) -> str:
        if spec.properties is None:
            docs = self.make_doc_lines(spec)
            docs_join = "\n".join(docs)
            docs_or_empty = f"\n{docs_join}" if docs else ""
            body = f"{spec.name} = {spec.as_type}{docs_or_empty}\n"
            return body
        else:
            lines = []
            if self.has_union(spec):
                lines.append("@serde.serde(tagging=serde.Untagged)\n")
            lines.append("@dataclasses.dataclass\n")
            lines.append(f"class {spec.name}:\n")
            docs = self.make_doc_lines(spec)
            lines.extend(f"    {line}\n" for line in docs)
            for prop in spec.properties:
                if iskeyword(prop.name):
                    lines.append(
                        f'    {prop.name}_: {prop.as_type} = dataclasses.field(metadata={{"serde_rename": "{prop.name}"}})\n'
                    )
                else:
                    lines.append(f"    {prop.name}: {prop.as_type}\n")
                docs = self.make_doc_lines(prop)
                lines.extend(f"    {line}\n" for line in docs)
            if not spec.properties:
                lines.append("    pass\n")
            return "".join(lines)

    typing_types: ClassVar[list[str]] = ["Any", "Literal", "Optional", "Union"]

    def generate_files_schemas(self, generated_path: Path) -> None:
        schema_dir = generated_path.joinpath("_schemas")
        schema_dir.mkdir(parents=True, exist_ok=True)
        imports = []
        alls = []
        for name, spec in self.schemas.items():
            spec.name = name
            if spec.as_type == "Any":
                spec.refs.remove("Any")
            module_name = to_snake_case(name)
            file = schema_dir.joinpath(f"_{module_name}.py")
            imports.append(f"from ._{module_name} import {name}\n")
            alls.append(f'    "{name}",\n')
            refs = set(spec.refs)
            typing_refs = []
            for typing_ref in self.typing_types:
                if typing_ref in refs:
                    refs.remove(typing_ref)
                    typing_refs.append(typing_ref)
            import_refs = "".join(
                f"from portone_server_sdk._openapi._schemas._{to_snake_case(ref)} import {ref}\n"
                for ref in sorted(refs)
            )
            typing = ", ".join(sorted(typing_refs))
            has_union = self.has_union(spec)
            import_serde = "import serde\n" if has_union else ""
            import_typing = typing and f"from typing import {typing}\n"
            import_dataclass = "" if spec.properties is None else "import dataclasses\n"
            with open(file, "wt") as f:
                f.write(f"""{import_dataclass}{import_serde}{import_typing}{import_refs}
{self.generate_schema(spec)}
""")
        with open(schema_dir.joinpath("__init__.py"), "wt") as f:
            f.write(f"""{"".join(imports)}
__all__ = [
{"".join(alls)}]
""")

    def generate_files_api(self, generated_path: Path) -> None:
        sync_path = generated_path.joinpath("_sync_api")
        async_path = generated_path.joinpath("_async_api")
        sync_path.mkdir(parents=True, exist_ok=True)
        async_path.mkdir(parents=True, exist_ok=True)
        imports = []
        extends = []
        for operation in self.operations:
            class_name = to_pascal_case(operation.name)
            method_name = to_snake_case(operation.name)
            imports.append(f"from ._{method_name} import {class_name}\n")
            extends.append(f"    {class_name},\n")
            docs = self.make_doc_lines_raw(operation)
            docs.append("")
            docs.append("Args:")
            args = []
            refs = set()
            param_args = []
            if operation.param.properties:
                for prop in operation.param.properties:
                    filtered = f"{prop.name}_" if iskeyword(prop.name) else prop.name
                    args.append(f"{filtered}: {prop.as_type},")
                    prop_docs = self.make_doc_lines_raw(prop)
                    if prop_docs:
                        docs.append(f"    {filtered} ({prop.as_type}): {prop_docs[0]}.")
                        docs.extend(f"        {line}" for line in prop_docs[1:] if line)
                    else:
                        docs.append(f"    {filtered} ({prop.as_type})")
                    param_args.append(f"{filtered}={prop.name},")
                    refs.update(prop.refs)
            query_args = []
            if operation.query.properties:
                for prop in operation.query.properties:
                    filtered = f"{prop.name}_" if iskeyword(prop.name) else prop.name
                    args.append(f"{filtered}: {prop.as_type},")
                    prop_docs = self.make_doc_lines_raw(prop)
                    if prop_docs:
                        docs.append(f"    {filtered} ({prop.as_type}): {prop_docs[0]}.")
                        docs.extend(f"        {line}" for line in prop_docs[1:] if line)
                    else:
                        docs.append(f"    {filtered} ({prop.as_type})")
                    query_args.append(f"{filtered}={filtered},")
                    refs.update(prop.refs)
            body_args = []
            if operation.body is not None:
                body_spec = self.schemas[operation.body]
                if body_spec.properties:
                    for prop in body_spec.properties:
                        filtered = (
                            f"{prop.name}_" if iskeyword(prop.name) else prop.name
                        )
                        args.append(f"{filtered}: {prop.as_type},")
                        prop_docs = self.make_doc_lines_raw(prop)
                        if prop_docs:
                            docs.append(
                                f"    {filtered} ({prop.as_type}): {prop_docs[0]}."
                            )
                            docs.extend(
                                f"        {line}" for line in prop_docs[1:] if line
                            )
                        else:
                            docs.append(f"    {filtered} ({prop.as_type})")
                        body_args.append(f"{filtered}={filtered},")
                refs.update(body_spec.refs)
                refs.add(operation.body)
                body_class = operation.body
            else:
                body_class = "Empty"
                refs.add("Empty")
            if operation.success is not None:
                refs.add(operation.success)
                success_class = operation.success
            else:
                success_class = "None"
            if operation.returns is not None:
                docs.append("")
                docs.append("Returns:")
                desc_lines = rst(operation.returns).strip().splitlines()
                if desc_lines:
                    docs.append(f"    {success_class}: {desc_lines[0]}")
                    docs.extend(f"        {line}" for line in desc_lines[1:])
            errors = []
            raises = []
            refs.add(operation.error)
            error_spec = self.schemas[operation.error]
            errors.extend(error_spec.as_type[len("Union[") : -1].split(", "))
            errors.sort()
            docs.append("")
            docs.append("Raises:")
            for variant in errors:
                variant_spec = self.schemas[variant]
                docs.append(f"    _errors.{variant}: {variant_spec.title}")
                refs.add(variant)
                raises.append(f"if isinstance(error_, {variant}):")
                raises.append(f"    raise _errors.{variant}(error_)")
            error_class = operation.error
            if docs:
                docs[0] = f'"""{docs[0]}'
                if len(docs) > 1:
                    docs.append('"""')
                else:
                    docs[-1] = f'{docs[-1]}"""'
            typing_refs = []
            for typing_ref in self.typing_types:
                if typing_ref in refs:
                    refs.remove(typing_ref)
                    typing_refs.append(typing_ref)
            import_api = ["ApiRequest", "ApiErrorResponse"]
            if "Empty" in refs:
                refs.remove("Empty")
                import_api.append("Empty")
            typing = ", ".join(typing_refs)
            import_typing = typing and f"from typing import {typing}\n"
            import_refs = []
            for ref in sorted(refs):
                module_name = to_snake_case(ref)
                import_refs.append(
                    f"from portone_server_sdk._openapi._schemas._{module_name} import {ref}\n"
                )
            args_join = "".join(f"\n        {arg}" for arg in args)
            docs_join = "".join(f"\n        {line}" for line in docs) if docs else ""
            param_join = "".join(f"\n            {arg}" for arg in param_args)
            param_list = f"({param_join}\n        )" if param_args else "()"
            query_join = "".join(f"\n            {arg}" for arg in query_args)
            query_list = f"({query_join}\n        )" if query_args else "()"
            body_join = "".join(f"\n            {arg}" for arg in body_args)
            body_list = f"({body_join}\n        )" if body_args else "()"
            raises_join = "".join(f"            {line}\n" for line in raises)
            return_data_or_none = (
                "\n        return response_.data" if success_class != "None" else ""
            )
            for is_async in [True, False]:
                async_def = "async def" if is_async else "def"
                await_self = "await self" if is_async else "self"
                api_client = (
                    "from portone_server_sdk._async import ApiClient"
                    if is_async
                    else "from portone_server_sdk._sync import ApiClient"
                )
                body = f"""import dataclasses
{import_typing}
from portone_server_sdk._api import {", ".join(import_api)}
from portone_server_sdk import _errors
{api_client}
{"".join(import_refs)}
{self.generate_schema(operation.param)}
{self.generate_schema(operation.query)}
@dataclasses.dataclass
class {class_name}Request(ApiRequest[{success_class}, {error_class}, {operation.param.name}, {operation.query.name}, {body_class}]):
    method = "{operation.method}"
    path = "{operation.path}"

@dataclasses.dataclass
class {class_name}(ApiClient):
    {async_def} {method_name}(
        self,{args_join}
    ) -> {operation.success}:{docs_join}
        param_ = {operation.param.name}{param_list}
        query_ = {operation.query.name}{query_list}
        body_ = {body_class}{body_list}
        response_ = {await_self}.send(
            {class_name}Request(param_, query_, body_),
            {operation.success},
            {operation.error},
        )
        if isinstance(response_, ApiErrorResponse):
            error_ = response_.data
{raises_join}{return_data_or_none}
"""
                path = async_path if is_async else sync_path
                with path.joinpath(f"_{method_name}.py").open("wt") as f:
                    f.write(body)
        init = f"""from dataclasses import dataclass
{"".join(imports)}
@dataclass
class PortOneApi(
{"".join(extends)}):
    pass
"""
        with async_path.joinpath("__init__.py").open("wt") as f:
            f.write(init)
        with sync_path.joinpath("__init__.py").open("wt") as f:
            f.write(init)


def to_snake_case(camel_case: str) -> str:
    return re.sub("[A-Z]", lambda groups: f"_{groups[0].lower()}", camel_case).lstrip(
        "_"
    )


def to_pascal_case(camel_case: str) -> str:
    return camel_case[:1].upper() + camel_case[1:]
