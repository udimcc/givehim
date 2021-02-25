from car import Car
from typing import List

def calculate_total_path_duration(car):
    result = 0
    for path in car.paths:
        result += path.L + 1

    return result - 1

def remove_non_realistic_cars(cars : List[Car], deadline : int):
    """Gets list of cars with their paths and returns list without the unrealistic cars"""
    for car in cars:
        if calculate_total_path_duration(car) >= deadline:
            cars.remove(car)

    return cars
