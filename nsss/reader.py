import tomlkit

# from dataclasses import dataclass
from collections import namedtuple
from pathlib import Path
from typing import Any, NamedTuple


def read_toml(path: Path) -> dict[str, Any]:
    return tomlkit.loads(path.read_text())


def dict_to_namedtuple(tuple_name: str, dictionary: dict[str, Any]) -> NamedTuple:
    """Converts a dictionary to a namedtuple."""

    NamedTupleClass = namedtuple(tuple_name, dictionary.keys())
    return NamedTupleClass(**dictionary)
