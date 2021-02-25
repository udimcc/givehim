from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Street:
	L : int # time
	start : int # Intersection (avoid circular import)
	end : int # Intersection
	name : str