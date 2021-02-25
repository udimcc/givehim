from dataclasses import dataclass
from street import Street
from typing import List
from inputparser import InputCluster
@dataclass
class Intersection:
	id : int
	in_streets : List[Street] # The point is this intersection
	out_streets : List[Street] # Traffic light here does not matter

def createIntersections(path):
	alldata = get_input(path)
	inters_ids = set()

	for street in alldata.streets:
		inters_ids.add(street.start)
		inters_ids.add(street.end)

	intersections = {id: Intersection(id, [], []) for id in inters_ids}

	for street in alldata.streets:
		intersections[street.start].out_streets.append(street)
		intersections[street.end].in_streets.append(street)

	return list(intersections.values())