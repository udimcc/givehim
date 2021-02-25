# %%
from car import Car
from path import Path
from dataclasses import dataclass
from typing import List

def get_input(file_path):
	with open(file_path) as f:
		deadline, num_intersections, num_streets, num_cars, fixed_bonus_points = f.readline().split()

		paths = []

		for i in range(int(num_streets)):
			start_intersection, end_intersection, street_name, length = f.readline().split()

			paths.append(Path(int(start_intersection), int(end_intersection), street_name, int(length)))

		car_paths = []

		for j in range(int(num_cars)):
			street_names = f.readline().split()[1:]

			car_paths.append(Car(street_names))
		
	return InputCluster(int(deadline), int(num_intersections), int(num_streets), int(num_cars), int(fixed_bonus_points),
						paths, car_paths)


@dataclass
class InputCluster:
	deadline : int
	num_intersections : int
	num_streets : int
	num_cars : int
	fixed_bonus_points : int
	paths : List[Path]
	car_paths : List[Car]

# %%
