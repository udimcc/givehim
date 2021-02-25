from dataclasses import dataclass
from street import Street
from typing import List

@dataclass
class Intersection:
	id : int
	in_streets : List[Street] # The point is this intersection
	out_streets : List[Street] # Traffic light here does not matter