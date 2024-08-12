# PortOne Server SDK for Python

## Prerequisite

- rye
- git-filter-repo

## Setup

```
git submodule update --init
rye sync
rye run init
```

## Scripts

- `init`
  - pre-commit 훅을 설정합니다.
- `gen`
  - 자동 생성이 필요한 코드를 생성합니다.
- `gen:env`
  - User Agent와 같은 빌드 타임 상수를 생성합니다.
- `gen:schema`
  - `openapi/v2.openapi.json`을 기반으로 스키마 코드를 생성합니다.
- `patch:save`
  - `portone_server_sdk/_openapi` local에 커밋된 내용을 바탕으로 patch 파일을 생성합니다.
- `patch:apply`
  - `portone_server_sdk/_openapi`에 patch를 적용합니다.
- `patch:clean`
  - `portone_server_sdk/_openapi` 디렉토리를 삭제합니다.
- `check`
  - 타입을 체크합니다.
- `docs`
  - API 문서를 생성합니다.

---

Packages under _portone-io/server-sdk-py_ are primarily distributed under the terms of
both the [Apache License (Version 2.0)] and the [MIT license]. See [COPYRIGHT]
for details.

[MIT license]: LICENSE-MIT
[Apache License (Version 2.0)]: LICENSE-APACHE
[COPYRIGHT]: COPYRIGHT
