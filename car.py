from path import Path
from dataclasses import dataclass
from typing import List

@dataclass
class Car:
	paths : List[Path]
