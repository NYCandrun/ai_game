# API catalog

- `specs/`: the 54 `swagger.json` files and the `domain_apis_list.json` of each of the 11 public `asdk_plugin_*` packages (PyPI, version 2.0.0b3), kept in their package paths, which encode the API name: `agraph/<domain>/<segment>/<group>/<version>/<API>`.
- `api_digest.txt`: one condensed file with every API's description, operations and main schemas, used for the briefings and the fact-check.
- `apis.json`: the list of APIs with domain, stability label (alpha, beta, stable, sunset) and operation counts.
- `aladdinsdk_README.md`: the AladdinSDK README from PyPI (configuration, run modes, Data Cloud and S3 clients).
