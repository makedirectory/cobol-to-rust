# Build Progress — cobol-to-rust

**Last updated:** 2026-07-15 · **Mode:** Clean-slate (beta) · **Latest:** v0.1

> Exposure / "wow" project: a COBOL→Rust transpiler scaffold. For **how** we work, see the shared
> **`PROCESS.md`** in the [cartograph-web docs handbook](https://github.com/makedirectory/cartograph-web/blob/main/apps/docs/docs/handbook/process.md). **Legend:** ⬜ · 🔄 · ✅ · ⚠️ · —

## Current snapshot

v0.1 transpiles a small COBOL subset (PROGRAM-ID, simple PIC, MOVE/ADD/SUBTRACT/MULTIPLY, DISPLAY,
STOP RUN) through an IR into a runnable Cargo project, with tests and CI that `cargo check`s the
output. The credibility line for later is **differential testing** (run COBOL vs generated Rust, diff).

### Active / next

| ID | Milestone | Impl | Tests | Docs | Reviewed | Status |
|----|-----------|:----:|:-----:|:----:|:--------:|:------:|
| v0.2 | Grammar-based parser; proper source normalization; structured parse errors | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| v0.3 | COBOL decimal arithmetic modeling (not everything → i64) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |
| v0.6 | Differential-testing harness (headline feature) | ⬜ | ⬜ | ⬜ | ⬜ | ⬜ |

## Shipped

| ID | Milestone | Impl | Tests | Docs | Reviewed | Status |
|----|-----------|:----:|:-----:|:----:|:--------:|:------:|
| v0.1 | Regex → IR → Rust codegen → Cargo project; CLI; CI (`cargo check`) | ✅ | ✅ | ✅ | ✅ | ✅ |
| — | OSS scaffolding; pinned `ruff==0.8.6` | ✅ | — | ✅ | ✅ | ✅ |

> **2026-07-15 — scaffolding + linter pin.** Apache-2.0 OSS scaffolding; ruff/mypy pinned to match
> pre-commit; beta banner added. **Review:** main CI green (incl. `cargo check` of generated output).
> **Deferred:** grammar parser (v0.2), decimal model (v0.3), differential tests (v0.6).

## Decision log

| Date | Decision | Reason |
|------|----------|--------|
| 2026-07-15 | Translate through an IR, never text→text | A serious converter needs a semantic layer |
| 2026-07-15 | Unsupported constructs must warn, never silently miscompile | Correctness/credibility contract |

---

*Companion: shared `PROCESS.md` (cartograph-web docs handbook).*
