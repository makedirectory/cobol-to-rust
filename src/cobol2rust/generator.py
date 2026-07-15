from __future__ import annotations

import re
from pathlib import Path

from .model import Program
from .parser import rust_name


def expression(token: str, string_context: bool = False) -> str:
    token = token.strip()
    if (token.startswith('"') and token.endswith('"')) or (token.startswith("'") and token.endswith("'")):
        content = token[1:-1].replace('"', '\\"')
        return f'"{content}"'
    if re.fullmatch(r"-?\d+", token):
        return token
    return rust_name(token)


def generate_main(program: Program) -> str:
    variable_types = {variable.name: variable.rust_type for variable in program.variables}
    lines = ["fn main() {"]
    for variable in program.variables:
        lines.append(f"    let mut {variable.name}: {variable.rust_type} = {variable.initial_value};")

    for statement in program.statements:
        op, args = statement.operation, statement.args
        if op == "move":
            source, target = args
            if variable_types.get(target) == "String":
                lines.append(f"    {target} = {expression(source)}.to_string();")
            else:
                lines.append(f"    {target} = {expression(source)};")
        elif op == "add":
            value, target = args
            lines.append(f"    {target} += {expression(value)};")
        elif op == "subtract":
            value, target = args
            lines.append(f"    {target} -= {expression(value)};")
        elif op == "multiply":
            target, value = args
            lines.append(f"    {target} *= {expression(value)};")
        elif op == "display":
            lines.append(f"    println!(\"{{}}\", {expression(args[0])});")
        elif op == "unsupported":
            escaped = args[0].replace("*/", "* /")
            lines.append(f"    /* unsupported COBOL: {escaped} */")
        elif op == "stop":
            lines.append("    return;")
    lines.append("}")
    return "\n".join(lines) + "\n"


def write_cargo_project(program: Program, output: Path) -> None:
    output.mkdir(parents=True, exist_ok=True)
    (output / "src").mkdir(exist_ok=True)
    package = program.name.lower().replace("_", "-")
    cargo = f'''[package]\nname = "{package}"\nversion = "0.1.0"\nedition = "2021"\n\n[dependencies]\n'''
    (output / "Cargo.toml").write_text(cargo, encoding="utf-8")
    (output / "src" / "main.rs").write_text(generate_main(program), encoding="utf-8")
