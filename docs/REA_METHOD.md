# REA method and limits

## Run performed

`rea-agents@6.8.0` installed in a temporary research environment with npm lifecycle scripts disabled. Its `--version` returned 6.8.0. No agent setup/config mutation was run. Nanobot application and provider calls were not started.

With the reviewed checkout available at `/absolute/path/to/nanobot`, the equivalent command is:

```sh
rea analyze-javascript-application /absolute/path/to/nanobot/webui \
  --source-path package.json \
  --source-path src/main.tsx \
  --source-path src/App.tsx \
  --source-path src/lib/nanobot-client.ts \
  --source-path src/lib/http.ts \
  --source-path src/lib/runtime.ts \
  --max-heap-mb 512 --analysis-timeout-ms 60000 --format json
```

Exit code 0. Terminal progress reported reconstruction complete for the selected scope. That is not whole-application completeness. See `evidence/rea-webui-summary.json`.

The extracted public summary omits local execution paths and does not reproduce the original Evidence JSON. Its evidence id references the privately retained original; the summary cannot independently verify that original hash. No raw assistant transcripts, credentials or account data are included. A fresh rerun against the same selected source may have environment/tool-version differences; compare source hashes and limitations, not only graph counts.

## Complementary Python analysis

Python standard-library `ast.parse` inventoried 541 files under `nanobot/`; zero parser errors. It did not import/execute the target, resolve dynamic imports, run tests or establish behavior. Public `python-ast-index.json` includes only upstream-relative paths, source hashes and top-level symbols/line numbers. It is not a REA output.

## Why scope matters

REA's inspected workflow is JavaScript/Electron static analysis, so it is suitable for selected Nanobot frontend files, not a complete Python runtime decompiler. No native engine was needed or installed. Static source offers more direct evidence than decompiling an available open-source codebase.

Source: https://github.com/morluto/rea/blob/main/docs/javascript-application-graph.md
Source: https://github.com/morluto/rea/blob/main/src/application/javascript/JavaScriptApplicationService.ts
