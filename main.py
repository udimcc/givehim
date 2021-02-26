# this file should be the main file that will be the final solution

from inputparser import get_input
from algorithm import *
from submit import *
import sys
from functools import lru_cache

def main():
	file_path = sys.argv[1] 
	print(f"Working on {file_path}")
	ic = get_input(file_path)

	all_street = tuple(ic.streets)

	intersection_lst = []
	for i in range(ic.num_intersections):
		intersection_lst.append(IntersectionWithSchedule(i,[]))
	streets_with_schedule, flowchart = omri_algorithm(ic.car_paths, ic.deadline,all_street)

	#changeWeight(intersections: List[Intersection], initialiFlowRet: InitialFlowRet, streetWithSchedule: list):
	#streets_with_schedule = rons_algorithm(ic.car_paths, flow_chart, streets_with_schedule)
	# = udi_algorithem(flowchart)
	sws_to_intersection_list(all_street, intersection_lst,streets_with_schedule)

	si = SubmitInfo(intersection_lst)

	submit_info_to_submit_file(f"output-{file_path.split('/')[-1]}", si)

	print("Started running ...")

@lru_cache
def get_street_by_name(all_street,name):
	for street in all_street:
		if street.name == name:
			return street

def sws_to_intersection_list(all_street, intersection_lst,streets_with_schedule):
	for sws in streets_with_schedule:
		intersection_lst[get_street_by_name(all_street,sws.street).end].streets_with_schedule.append(sws)
	for strt in all_street:
		if not strt.name in intersection_lst[strt.end].streets_with_schedule:
			intersection_lst[strt.end].streets_with_schedule.append(StreetWithSchedule(strt.name,0))


if __name__ == '__main__':
	main()
