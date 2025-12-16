<div align="center">

# tap-fedidb

<div>
  <a href="https://github.com/reservoir-data/tap-fedidb/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/reservoir-data/tap-fedidb"/>
  </a>
  <a href="https://results.pre-commit.ci/latest/github/reservoir-data/tap-fedidb/main">
    <img alt="pre-commit.ci status" src="https://results.pre-commit.ci/badge/github/reservoir-data/tap-fedidb/main.svg"/>
  </a>
  <a href="https://scientific-python.org/specs/spec-0000/">
    <img alt="SPEC 0 — Minimum Supported Dependencies" src="https://img.shields.io/badge/SPEC-0-green"/>
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff" style="max-width:100%;">
  </a>
  <a href="https://github.com/astral-sh/uv">
   <img alt="uv" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json"/>
  </a>
  <a href="https://pypi.org/p/tap-fedidb/">
    <img alt="Python versions" src="https://img.shields.io/pypi/pyversions/tap-fedidb"/>
  </a>
</div>

Singer tap for [FediDB.org](https://fedidb.org).

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

</div>

# Capabilities

* `catalog`
* `state`
* `discover`
* `about`
* `stream-maps`
* `schema-flattening`
* `batch`

## Supported Python Versions

* 3.12
* 3.13
* 3.14

## Settings

This tap doesn't have any settings of its own, but it does support the following built-in SDK settings:

| Setting                           | Required | Default | Description                                                                                                                                                                                                                                              |
| :-------------------------------- | :------- | :------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| stream_maps                       | False    | None    | Config object for stream maps capability. For more information check out [Stream Maps](https://sdk.meltano.com/en/latest/stream_maps.html).                                                                                                              |
| stream_map_config                 | False    | None    | User-defined config values to be used within map expressions.                                                                                                                                                                                            |
| faker_config                      | False    | None    | Config for the [`Faker`](https://faker.readthedocs.io/en/master/) instance variable `fake` used within map expressions. Only applicable if the plugin specifies `faker` as an addtional dependency (through the `singer-sdk` `faker` extra or directly). |
| faker_config.seed                 | False    | None    | Value to seed the Faker generator for deterministic output: https://faker.readthedocs.io/en/master/#seeding-the-generator                                                                                                                                |
| faker_config.locale               | False    | None    | One or more LCID locale strings to produce localized output for: https://faker.readthedocs.io/en/master/#localization                                                                                                                                    |
| flattening_enabled                | False    | None    | 'True' to enable schema flattening and automatically expand nested properties.                                                                                                                                                                           |
| flattening_max_depth              | False    | None    | The max depth to flatten schemas.                                                                                                                                                                                                                        |
| batch_config                      | False    | None    |                                                                                                                                                                                                                                                          |
| batch_config.encoding             | False    | None    | Specifies the format and compression of the batch files.                                                                                                                                                                                                 |
| batch_config.encoding.format      | False    | None    | Format to use for batch files.                                                                                                                                                                                                                           |
| batch_config.encoding.compression | False    | None    | Compression format to use for batch files.                                                                                                                                                                                                               |
| batch_config.storage              | False    | None    | Defines the storage layer to use when writing batch files                                                                                                                                                                                                |
| batch_config.storage.root         | False    | None    | Root path to use when writing batch files.                                                                                                                                                                                                               |
| batch_config.storage.prefix       | False    | None    | Prefix to use when writing batch files.                                                                                                                                                                                                                  |

A full list of supported settings and capabilities is available by running: `tap-fedidb --about`

### Source Authentication and Authorization

The FediDB API doesn't require authentication at this time.

## Usage

You can easily run `tap-fedidb` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-fedidb --version
tap-fedidb --help
tap-fedidb --config CONFIG --discover > ./catalog.json
```

## Developer Resources

### Initialize your Development Environment

You will need the following tools to develop and test this tap:

- Python 3.12+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

### Create and Run Tests

Run integration tests:

```bash
uvx --with=tox-uv tox -e 3.12
```

You can also test the `tap-fedidb` CLI interface directly:

```bash
uvx --with=tox-uv tox -e sync
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Go ahead and [install Meltano](https://docs.meltano.com/getting-started/installation/) if you haven't already.

1. Install all plugins

   ```bash
   meltano install
   ```

1. Check that the extractor is working properly

   ```bash
   meltano invoke tap-fedidb --version
   ```

1. Execute an ELT pipeline

   ```bash
   meltano run tap-fedidb target-jsonl
   ```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
