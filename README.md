# Cloud9-MoneyMatter

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

## Release tracking, source and rollback

Canonical live OAuth patch hashes remain in the private `Cloud9-local-Patches` registry. This repository tracks the rebased patch and validation proof; it does **not** duplicate the full upstream application or include database contents.

Release watcher: `.github/workflows/upstream-watch.yml` checks stable upstream tags weekly and opens an issue if `v0.33.14` has changed. A new upstream release is not auto-deployed. Validate OAuth token exchange with MCPProxy, PostgreSQL migrations, frontend parity and rollback first. Do not change production data from CI.

Original application: https://github.com/letehaha/moneymatter. Public historical GitHub fork `GodsQuantum/moneymatter` cannot be made private while it remains in GitHub's fork network; this **private standalone overlay** is canonical for Cloud9.
