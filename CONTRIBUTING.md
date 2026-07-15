# Contributing to COBOL to Rust Converter

Thanks for your interest! This is an educational, extensible transpiler scaffold.
The goal is that every supported construct is understandable, tested, and
**verified against real COBOL** — never silently miscompiled.

Please also read the [Code of Conduct](CODE_OF_CONDUCT.md) and the
[roadmap](docs/ROADMAP.md) / [spec](docs/SPEC.md) before large changes.

## Development setup

Requirements: Python 3.11+, a Rust toolchain (`cargo`), and (for differential
testing) GnuCOBOL (`cobc`).

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e '.[dev]'

cobol2rust examples/hello.cbl --output build/hello-rust
cd build/hello-rust && cargo run
```

## Before you open a PR

```bash
pytest -q                  # tests
ruff check .               # lint
ruff format --check .      # formatting
mypy src                   # type-check
```

Install `pre-commit install` to run lint/format automatically on commit.

## Guidelines

- Translate through the **IR**, never COBOL text directly to Rust.
- Any construct whose Rust semantics may differ from COBOL **must emit a warning** —
  see the semantics-preservation policy in `docs/SPEC.md`. Silent miscompilation is
  the one unacceptable bug.
- Add parser tests (expected IR) and codegen tests (generated Rust compiles/runs)
  for every new construct. Prefer differential tests where feasible.
- Keep the supported-subset matrix in the README and `docs/SPEC.md` current.

## Licensing of contributions

By submitting a contribution, you agree it is licensed under the project's
[Apache License 2.0](LICENSE).
