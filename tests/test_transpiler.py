from pathlib import Path

from cobol2rust.generator import generate_main
from cobol2rust.parser import parse_program


def test_example_generates_rust() -> None:
    source = (Path(__file__).parents[1] / "examples" / "hello.cbl").read_text()
    rust = generate_main(parse_program(source))
    assert 'println!("{}", message);' in rust
    assert "counter += 2;" in rust
