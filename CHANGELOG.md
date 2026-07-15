# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Open-source scaffolding: `LICENSE` (Apache-2.0), `NOTICE`, `CONTRIBUTING`,
  `CODE_OF_CONDUCT`, `SECURITY`, issue/PR templates, `CODEOWNERS`, Dependabot,
  pre-commit, and `docs/ROADMAP.md` + `docs/SPEC.md`.

## [0.1.0]

### Added
- Regex parser for a small COBOL subset → IR → Rust code generator → Cargo project.
- Support for `PROGRAM-ID`, simple `PIC` variables, `MOVE`/`ADD`/`SUBTRACT`/
  `MULTIPLY`, `DISPLAY`, and `STOP RUN`.
- `cobol2rust` CLI, tests, and CI (including `cargo check` of generated output).

[Unreleased]: https://github.com/makedirectory/cobol-to-rust/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/makedirectory/cobol-to-rust/releases/tag/v0.1.0
