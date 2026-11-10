# Cloud9-local-MoneyMatter

Private Cloud9 patch overlay for https://github.com/letehaha/moneymatter (upstream branch dev).
The public GodsQuantum/moneymatter fork exists and is kept unchanged; upstream has its own FR locale already.
The only known essential divergence is the Cloud9-compatible OAuth RFC6749 token response used by MCPProxy.

On 2026-11-09 the patched upstream source (f1207ed1354de17b58b16a499563fa698fd92f67) passed:
- npm ci
- targeted backend unit tests
- backend TypeScript typechecking

This repo stores only the isolated patch and evidence, not cloned upstream, not private data, and not live deployment config.
New upstream versions should attempt the patch on fresh source, inspect upstream OAuth support, run tests, and only then build/publish GHCR and deploy via Komodo.
Do not overwrite production MoneyMatter database or use an unvalidated frontend/backend upgrade.
