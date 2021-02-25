import random
from enum import Enum
from typing import Tuple
from intersection import Intersection
from street import Street

class ChooseOrderStrategy(Enum):
    RANDOM,
    SUPER_SMART_ALGO


def choose_order(intersections: Tuple[Intersection], scheduled_streets: Tuple[StreetWithSchedule], flow_chart: InitialFlowRet):
    inter_street_order = {}

    for inter in intersections:
        streets = inter.in_streets
        relevant_scheduled_streets = tuple(s for s in scheduled_streets if s.street in streets)
        streets_order = choose_order_per_intersection(relevant_scheduled_streets, flow_chart)
        inter_street_order[inter] = streets_order

    return inter_street_order


def choose_order_per_intersection(scheduled_streets: Tuple[StreetWithSchedule], flow_chart: InitialFlowRet): #Tuple[Streets...]
    for scheduled_street in scheduled_street:
        if scheduled_street.street == most_busy_inter:
            most_busy_street_time = inter_times[most_busy_inter]
            break

    times = tuple(s.duration for most_busy_street_time in scheduled_street)

    for most_busy_inter_place in range(len(scheduled_streets)):
        for scheduled_street in scheduled_streets:
            start = scheduled_street.duration
            time = get_max_window(start, most_busy_street_time, times)

