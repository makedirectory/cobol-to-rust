# cobol-to-rust — Roadmap

**Funnel role:** top-of-funnel attention/"wow" magnet (see `../../STRATEGY.md`).
**Investment posture:** staged and honest. A general COBOL→Rust converter is a major compiler effort;
this repo is a *credible, growing scaffold*, not a claim of full automated conversion.
**License:** Apache-2.0. The credibility hook is **differential testing** (§ below), not subset size.

Each supported-construct milestone is a shareable content beat.

## v0.1 — current
- Regex parse of a tiny subset → IR → Rust codegen → runnable Cargo project.
- Supports: `PROGRAM-ID`, simple `PIC` vars, `MOVE`/`ADD`/`SUBTRACT`/`MULTIPLY`, `DISPLAY`, `STOP RUN`.

## v0.2 — real front end
- Replace regex with a grammar-based lexer/parser (tree-sitter or hand-written recursive descent).
- Proper source normalization (fixed-format columns, continuations, comments).
- Structured parse errors with line/column.

## v0.3 — decimal semantics (the credibility line)
- Model COBOL decimal arithmetic (fixed-point / `PIC 9V99`) instead of mapping everything to `i64`.
- Choose a Rust decimal representation; document precision/rounding behavior.
- **Content:** "Why COBOL money math doesn't fit in an integer — and how we model it in Rust."

## v0.4 — control flow
- Paragraphs + `PERFORM` (incl. `THRU`, `TIMES`); `IF`, `EVALUATE`, `88`-level condition names.

## v0.5 — data structures
- Group items, `OCCURS`, `REDEFINES`, `PIC` editing basics.

## v0.6 — differential testing harness (make this loud)
- Run the original COBOL (GnuCOBOL) and the generated Rust on the same fixtures; diff outputs.
- Emit **warnings whenever semantics cannot be preserved exactly** (never silently miscompile).
- **Content:** "We transpile COBOL to Rust and prove it with differential testing."

## Later — the hard estate features (mostly out of scope for OSS marketing repo)
- Copybook resolution, embedded SQL preprocessing, file organizations (indexed/relative), CICS.
- These overlap the paid modernization work — treat as consulting/product, not free-repo scope creep.

## Explicit non-goals
- Full COBOL dialect coverage or "point it at your mainframe" automation.
- Correctness without differential evidence — unproven constructs must warn, not pretend.

## Success signals
- HN/Reddit/GitHub traction on each new construct + the differential-testing story.
- Inbound "can you convert *our* COBOL?" → routes to services / the toolkit.
