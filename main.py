# this file should be the main file that will be the final solution

from inputparser import get_input, get_street_by_name
from algorithm import *
from submit import *
from time import time
import sys
from multiprocessing import Process

def main(file_path):
	initial_time = time()
	print(f"Working on {file_path}")
	ic = get_input(file_path)
	print(f"Started running ...{file_path} {time()-initial_time}",)

	all_street = tuple(ic.streets)

	intersection_lst = []
	for i in range(ic.num_intersections):
		intersection_lst.append(IntersectionWithSchedule(i,[]))
	streets_with_schedule, flowchart = omri_algorithm(ic.car_paths, ic.deadline,all_street)
	print(f"finished with omri_algorithm in {file_path} {time()-initial_time}")

	#changeWeight(intersections: List[Intersection], initialiFlowRet: InitialFlowRet, streetWithSchedule: list):
	#streets_with_schedule = rons_algorithm(ic.car_paths, flow_chart, streets_with_schedule)
	# = udi_algorithem(flowchart)
	sws_to_intersection_list(all_street, intersection_lst,streets_with_schedule)

	print(f"finished with creating intersection_lst in {file_path} {time()-initial_time}")
	si = SubmitInfo(intersection_lst)

	submit_info_to_submit_file(f"output-{file_path.split('/')[-1]}", si)

	print(f"{file_path} is FINISHED in {time()-initial_time}")

def sws_to_intersection_list(all_street, intersection_lst,streets_with_schedule):
	for sws in streets_with_schedule:
		intersection_lst[get_street_by_name(all_street,sws.street).end].streets_with_schedule.append(sws)
	for strt in all_street:
		if not strt.name in [stwsc.street for stwsc in intersection_lst[strt.end].streets_with_schedule]:
			intersection_lst[strt.end].streets_with_schedule.append(StreetWithSchedule(strt.name,0))


if __name__ == '__main__':
	for fp in sys.argv[1:]:
		p = Process(target=main, args=(fp,))
		p.start()
		# main(fp)
