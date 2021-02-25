from typing import Tuple, Dict
from dataclasses import dataclass
from collections import defaultdict
from car import Car
from street import Street

CarsStatuses = Dict[Car, int]

@dataclass
class InitialFlowRet:
    car_end_times: CarsStatuses
    car_street_times: Dict[Street, CarsStatuses]

def get_initial_flow(cars: Tuple[Car]) -> InitialFlowRet:
    car_end_times = {}
    car_street_times = defaultdict(dict)

    for car in cars:
        accumulate_street_time = 0
        for street in car.paths:
            accumulate_street_time += street.L
            car_street_times[street][car] = accumulate_street_time
        
        car_end_times[car] = accumulate_street_time

    return InitialFlowRet(car_end_times, car_street_times)

