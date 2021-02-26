from car import Car
from submit import StreetWithSchedule
from typing import List
from flow_chart import get_initial_flow
from functools import lru_cache

@lru_cache
def get_street_by_name(all_street,name):
    for street in all_street:
        if street.name == name:
            return street

def calculate_total_path_duration(car : Car,all_street):
    result = 0
    for path in car.paths:
        result += path.L + 1

    return result - 1

def remove_non_realistic_cars(cars : List[Car], deadline : int,all_street):
    """Gets list of cars with their paths and returns list without the unrealistic cars"""
    for car in cars:
        if calculate_total_path_duration(car,all_street) >= deadline:
            cars.remove(car)

    return cars

def get_sequenced_times(times : List[int]):
    seq = 0
    last_time = times[0]

    for time in times:
        if time > last_time + 1:
            return seq
        seq += 1
        last_time = time

    return 1

def get_avg_sequenced_times(times : List[int]):
    sequences = []

    while len(times) != 0:
        curr_seq = get_sequenced_times(times)
        times = times[curr_seq:]
        sequences.append(curr_seq)

    avg = 0
    for sequence in sequences:
        avg += sequence

    avg /= len(sequences)
    return int(avg)

def omri_algorithm(cars : List[Car], deadline,all_street):
    cars = remove_non_realistic_cars(cars,deadline,all_street)

    flowchart = get_initial_flow(cars)
    streets_traffics = { street: list(sorted_arrivals.values()) for street, sorted_arrivals in flowchart.car_street_times.items()}

    out = []

    for street, times in streets_traffics.items():
        out.append(StreetWithSchedule(street.name, get_avg_sequenced_times(list(times))))

    return (out, flowchart)
