from dataclasses import dataclass
from traffic_light import TrafficLight
from car import Car
from typing import List
from path import Path

@dataclass
class Street:
	path : Path
	traffic_light : TrafficLight # The traffic at the end
	waiting_cars : List[Car] # But actually a queue