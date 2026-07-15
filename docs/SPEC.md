# cobol-to-rust — Technical Spec

## Purpose
An educational, extensible COBOL→Rust transpiler **scaffold**. Optimized so every generated construct
is understandable and testable, and so the pipeline can grow from regex into a real compiler front end.

## Pipeline
```
COBOL source
  → source normalization (strip cols 1-6 & 73+, drop comments, join continuations)
  → parser  (v0.1 regex → v0.2 grammar-based)
  → IR / semantic model (Program, Variable, Statement)
  → Rust code generator
  → generated Cargo project
```
**The IR boundary is load-bearing:** never translate COBOL text directly to Rust. The semantic layer
owns data layout, decimal behavior, control flow, and (later) file I/O and runtime compatibility.

## IR model (current → target)
- `Program(name, variables, statements)`
- `Variable(name, rust_type, initial)` — v0.1 maps `PIC X`→`String`, numeric→`i64`.
  **v0.3 replaces `i64` with a decimal type** carrying precision/scale from the `PIC`.
- `Statement(kind, args)` — kinds: `move|add|subtract|multiply|display|stop|unsupported`.
  `unsupported` is intentional: unknown constructs are preserved + surfaced, never dropped.

## Supported-subset matrix (keep current in README)
| Construct | Status |
|-----------|--------|
| PROGRAM-ID, simple PIC 9/S9/X | ✅ v0.1 |
| MOVE/ADD/SUBTRACT/MULTIPLY, DISPLAY, STOP RUN | ✅ v0.1 |
| Grammar-based parse, decimal arithmetic | ▶ v0.2–v0.3 |
| PERFORM, IF, EVALUATE, 88-levels | ▶ v0.4 |
| Groups, OCCURS, REDEFINES | ▶ v0.5 |
| Copybooks, embedded SQL, CICS, file I/O | ✗ out of marketing-repo scope |

## Semantics-preservation policy (the credibility contract)
- Any construct whose Rust translation may differ from COBOL semantics **must emit a warning** (compile-
  time note in output + a comment in generated code). Silent miscompilation is the one unacceptable bug.
- Decimal rounding, truncation, and overflow behavior must be documented per construct.

## Testing strategy
- Unit: parser produces expected IR for each supported construct.
- Codegen: generated Rust compiles (`cargo build`) and runs.
- **Differential (v0.6, headline feature):** run GnuCOBOL and generated Rust on shared fixtures; assert
  identical stdout/values; failures block release.

## Non-goals
Full dialect coverage, mainframe automation, or any "converts your estate" claim. This is a scaffold and
a proof-of-approach — see the scope warning in the README.
