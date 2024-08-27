# 기여 가이드

## Prerequisite

- uv
- git-filter-repo

## Setup

```
uv sync
uvx run pre-commit install
```

## Scripts

- `uv run scripts/gen-env.py`
  - User Agent와 같은 빌드 타임 상수를 생성합니다.
- `uv run scripts/rebuild-schema.py`
  - `openapi/v2.openapi.json`을 기반으로 스키마 코드를 생성합니다.
- `uv run scripts/patch.py save`
  - `portone_server_sdk/_openapi` local에 커밋된 내용을 바탕으로 patch 파일을 생성합니다.
- `uv run scripts/patch.py apply`
  - `portone_server_sdk/_openapi`에 patch를 적용합니다.
- `uv run scripts/patch.py clean`
  - `portone_server_sdk/_openapi` 디렉토리를 삭제합니다.
- `uv run pyright`
  - 타입을 체크합니다.
- `uv run mkdocs build`
  - API 문서를 생성합니다.
