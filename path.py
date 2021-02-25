from dataclasses import dataclass

@dataclass
class Path:
	L : int # time
	start : int # Intersection (avoid circular import)
	end : int # Intersection
	name : str