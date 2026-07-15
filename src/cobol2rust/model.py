from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Variable:
    name: str
    rust_type: str
    initial_value: str


@dataclass(frozen=True)
class Statement:
    operation: str
    args: tuple[str, ...]


@dataclass(frozen=True)
class Program:
    name: str
    variables: tuple[Variable, ...]
    statements: tuple[Statement, ...]
