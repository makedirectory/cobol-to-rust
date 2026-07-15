# COBOL to Rust Converter

[![CI](https://github.com/makedirectory/cobol-to-rust/actions/workflows/ci.yml/badge.svg)](https://github.com/makedirectory/cobol-to-rust/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![Status: beta](https://img.shields.io/badge/status-beta-orange)

> **Beta — in active development.** An experimental scaffold, not a full converter; interfaces and
> supported subset will change. We'd love feedback — [open an issue](https://github.com/makedirectory/cobol-to-rust/issues).

An educational, extensible COBOL-to-Rust transpiler scaffold.

It supports a deliberately small COBOL subset so that every generated construct is understandable and testable. The project is structured to grow from regex parsing into a real lexer/parser, semantic model, and compatibility runtime.

## Supported subset

- `PROGRAM-ID`
- Working-storage variables using simple `PIC 9(...)`, `PIC S9(...)`, and `PIC X(...)`
- `MOVE literal TO variable`
- `ADD value TO variable`
- `SUBTRACT value FROM variable`
- `MULTIPLY variable BY value`
- `DISPLAY` literals and variables
- `STOP RUN`

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'

cobol2rust examples/hello.cbl --output build/hello-rust
cd build/hello-rust
cargo run
```

Expected output:

```text
HELLO FROM COBOL
42
```

Run tests:

```bash
pytest
```

## Architecture

```text
COBOL source
  -> source normalization
  -> parser
  -> intermediate representation (IR)
  -> Rust code generator
  -> generated Cargo project
```

The IR boundary is important: a serious converter should not translate text directly from COBOL into Rust. It needs a semantic layer for data layout, decimal behavior, control flow, file I/O, and runtime compatibility.

## Recommended roadmap

1. Replace regex parsing with a grammar-based parser.
2. Model COBOL decimal arithmetic rather than mapping everything to Rust integers.
3. Add paragraph and `PERFORM` control-flow support.
4. Support `IF`, `EVALUATE`, `88` levels, groups, and `REDEFINES`.
5. Add copybook resolution and embedded SQL preprocessing.
6. Build a compatibility runtime for fixed-width records and indexed files.
7. Implement differential tests: run COBOL and generated Rust with the same fixtures and compare outputs.
8. Emit warnings whenever semantics cannot be preserved exactly.

## Scope warning

A general-purpose COBOL-to-Rust converter is a major compiler and migration effort. COBOL semantics include decimal arithmetic, fixed-format source, record layouts, `REDEFINES`, file organizations, vendor dialects, CICS, embedded SQL, and decades of application-specific conventions. This repository is a credible starting point, not a claim of full automated conversion.

## Roadmap & design

See [`docs/ROADMAP.md`](docs/ROADMAP.md) and [`docs/SPEC.md`](docs/SPEC.md) (incl. the semantics-preservation policy).

## Part of the COBOL Modernization Starters

- **[cobol-rest-bridge](https://github.com/makedirectory/cobol-rest-bridge)** — expose COBOL through REST
- **[cobol-migration-toolkit](https://github.com/makedirectory/cobol-migration-toolkit)** — inventory & dependency analysis
- **[cobol-to-rust](https://github.com/makedirectory/cobol-to-rust)** — a COBOL-to-Rust transpiler scaffold (this repo)

## Contributing

Contributions welcome — see [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md). Report vulnerabilities per [SECURITY.md](SECURITY.md).

## License & commercial support

Licensed under the [Apache License 2.0](LICENSE). © 2026 Make Directory Developers, LLC.

Evaluating COBOL-to-Rust or another target for a real migration? Make Directory Developers offers mainframe & COBOL modernization services — [mk-dir.com](https://mk-dir.com) · andrew@mk-dir.com.
