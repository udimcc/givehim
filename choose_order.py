import random
from typing import Tuple
from intersection import Intersection
from street import Street


def choose_order(intersections: Tuple[Intersection], scheduled_streets: Tuple[StreetWithSchedule]):
    inter_street_order = {}

    for inter in intersections:
        streets = inter.in_streets
        relevant_scheduled_streets = tuple(s for s in scheduled_streets if s.street in streets)
        streets_order = choose_order_per_intersection(relevant_scheduled_streets)
        inter_street_order[inter] = streets_order

    return inter_street_order


def choose_order_per_intersection(scheduled_streets: Tuple[StreetWithSchedule]): #Tuple[Streets...]
    return random.shuffle(s.street for s in scheduled_streets)
