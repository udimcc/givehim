# this file should be the main file that will be the final solution

from inputparser import get_input
from algorithm import *
from submit import *

file_path = "data-sets/c.txt"


def main():
	ic = get_input(file_path)

	all_street = ic.streets

	intersection_lst = []
	for i in range(ic.num_intersections):
		intersection_lst.append(IntersectionWithSchedule(i,[]))
	streets_with_schedule, flowchart = omri_algorithm(ic.car_paths, ic.deadline,all_street)

	#changeWeight(intersections: List[Intersection], initialiFlowRet: InitialFlowRet, streetWithSchedule: list):
	#streets_with_schedule = rons_algorithm(ic.car_paths, flow_chart, streets_with_schedule)
	# = udi_algorithem(flowchart)
	sws_to_intersection_list(all_street, intersection_lst,streets_with_schedule)

	si = SubmitInfo(intersection_lst)

	submit_info_to_submit_file("output.txt", si)

	print("Started running ...")

def get_street_by_name(all_street,name):
	for street in all_street:
		if street.name == name:
			return street

def sws_to_intersection_list(all_street, intersection_lst,streets_with_schedule):
	for sws in streets_with_schedule:
		intersection_lst[get_street_by_name(all_street,sws.street).end].streets_with_schedule.append(sws)


if __name__ == '__main__':
	main()
