from dataclasses import dataclass
from typing import Tuple, Text
from street import Street

@dataclass(frozen=True)
class Car:
	paths : Tuple[Street]
