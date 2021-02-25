from dataclasses import dataclass
from enum import Enum

class Color(Enum):
	Red = True
	Green = False

@dataclass
class TrafficLight:
	state : Color

