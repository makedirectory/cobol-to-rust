from __future__ import annotations

import argparse
from pathlib import Path

from .generator import write_cargo_project
from .parser import parse_program


def main() -> None:
    parser = argparse.ArgumentParser(prog="cobol2rust")
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    program = parse_program(args.source.read_text(encoding="utf-8", errors="replace"))
    write_cargo_project(program, args.output)
    print(f"Generated Rust project at {args.output}")


if __name__ == "__main__":
    main()
