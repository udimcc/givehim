# %%
from car import Car
from street import Street
from dataclasses import dataclass
from typing import List
from functools import lru_cache

@lru_cache
def get_street_by_name(all_street,name):
    for street in all_street:
        if street.name == name:
            return street

def get_input(file_path):
	with open(file_path) as f:
		deadline, num_intersections, num_streets, num_cars, fixed_bonus_points = f.readline().split()

		streets = []

		for i in range(int(num_streets)):
			start_intersection, end_intersection, street_name, length = f.readline().split()

			streets.append(Street(int(length), int(start_intersection), int(end_intersection), street_name ))

		streets_as_tuple = tuple(streets)

		car_paths = []

		for j in range(int(num_cars)):
			street_names = f.readline().split()[1:]
			car_paths.append(Car(tuple([get_street_by_name(streets_as_tuple,streetname) for streetname in street_names])))
		
	return InputCluster(int(deadline), int(num_intersections), int(num_streets), int(num_cars), int(fixed_bonus_points),
						streets, car_paths)


@dataclass
class InputCluster:
	deadline : int
	num_intersections : int
	num_streets : int
	num_cars : int
	fixed_bonus_points : int
	streets : List[Street]
	car_paths : List[Car]

# %%
