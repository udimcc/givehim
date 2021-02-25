from typing import List, Tuple, Dict
from dataclasses import dataclass
from car import Car
from street import Street

CarStatus = Dict[Car, int]

@dataclass
class InitialFlowRet:
    car_end_times: CarStatus
    car_street_times: Dict[Street, CarStatus]

def get_initial_flow(cars: List[Car]) -> InitialFlowRet:
    pass

