from dataclasses import dataclass
from typing import List, Text
from street import Street

@dataclass(frozen=True)
class Car:
	paths : List[Street]
