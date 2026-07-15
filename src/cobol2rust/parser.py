from __future__ import annotations

import json
import re

from .model import Program, Statement, Variable

PROGRAM_ID = re.compile(r"PROGRAM-ID\.\s+([A-Z0-9_-]+)", re.IGNORECASE)
VARIABLE = re.compile(
    r"^\s*\d{2}\s+([A-Z0-9-]+)\s+PIC\s+([A-Z0-9V()]+)(?:\s+VALUE\s+([^\.]+))?\.",
    re.IGNORECASE | re.MULTILINE,
)


def normalize(text: str) -> str:
    lines = []
    for line in text.splitlines():
        if len(line) >= 7 and line[6] in {"*", "/"}:
            continue
        lines.append(line[7:72] if len(line) > 7 else line)
    return "\n".join(lines)


def rust_name(name: str) -> str:
    return name.lower().replace("-", "_")


def parse_value(value: str | None, rust_type: str) -> str:
    if value is None:
        return "String::new()" if rust_type == "String" else "0"
    value = value.strip().strip('"').strip("'")
    return f"{json.dumps(value)}.to_string()" if rust_type == "String" else value


def parse_program(text: str) -> Program:
    source = normalize(text)
    program_match = PROGRAM_ID.search(source)
    if not program_match:
        raise ValueError("PROGRAM-ID was not found")

    variables = []
    for name, picture, value in VARIABLE.findall(source):
        rust_type = "String" if "X" in picture.upper() else "i64"
        variables.append(Variable(rust_name(name), rust_type, parse_value(value or None, rust_type)))

    procedure = source.upper().split("PROCEDURE DIVISION.", 1)
    if len(procedure) != 2:
        raise ValueError("PROCEDURE DIVISION was not found")
    body_original = source[source.upper().index("PROCEDURE DIVISION.") + len("PROCEDURE DIVISION.") :]

    statements: list[Statement] = []
    for raw in body_original.splitlines():
        line = raw.strip().rstrip(".")
        if not line or re.fullmatch(r"[A-Z0-9-]+", line, re.IGNORECASE):
            continue
        upper = line.upper()
        if upper == "STOP RUN":
            statements.append(Statement("stop", ()))
        elif match := re.match(r"MOVE\s+(.+?)\s+TO\s+([A-Z0-9-]+)$", line, re.IGNORECASE):
            statements.append(Statement("move", (match.group(1), rust_name(match.group(2)))))
        elif match := re.match(r"ADD\s+(.+?)\s+TO\s+([A-Z0-9-]+)$", line, re.IGNORECASE):
            statements.append(Statement("add", (match.group(1), rust_name(match.group(2)))))
        elif match := re.match(r"SUBTRACT\s+(.+?)\s+FROM\s+([A-Z0-9-]+)$", line, re.IGNORECASE):
            statements.append(Statement("subtract", (match.group(1), rust_name(match.group(2)))))
        elif match := re.match(r"MULTIPLY\s+([A-Z0-9-]+)\s+BY\s+(.+?)$", line, re.IGNORECASE):
            statements.append(Statement("multiply", (rust_name(match.group(1)), match.group(2))))
        elif match := re.match(r"DISPLAY\s+(.+)$", line, re.IGNORECASE):
            statements.append(Statement("display", (match.group(1),)))
        else:
            statements.append(Statement("unsupported", (line,)))

    return Program(program_match.group(1), tuple(variables), tuple(statements))
