from dataclasses import dataclass
from typing import List

@dataclass
class StreetWithSchedule:
	street : str # Intersection or id
	duration : int # duration of green light

@dataclass
class IntersectionWithSchedule:
	intersection : int # Intersection or id
	streets_with_schedule : List[StreetWithSchedule] # the first one are the first r

@dataclass
class SubmitInfo():
	intersections : List[IntersectionWithSchedule]

def submit_info_to_submit_file(sf_path, si : SubmitInfo):
	lines_list = []
	si.intersections = [inter for inter in si.intersections if len(inter.streets_with_schedule) > 0]

	lines_list.append(str(len(si.intersections)))

	for intersection in si.intersections:
		lines_list.append(str(intersection.intersection))
		lines_list.append(str(len(intersection.streets_with_schedule)))
		for street_with_schedule in intersection.streets_with_schedule:
			lines_list.append(f"{street_with_schedule.street} {str(street_with_schedule.duration)}")

	with open(sf_path,'w') as sf:
		#sf.writelines(lines_list)
		sf.write('\n'.join(lines_list) + '\n')

def submit_file_to_submit_info(sf_path ,librarys):
	print("not Implemented") # doesnt worth the time
	exit(1)
	# with open(sf_path) as sf:
	# 	librarys_selected_with_books = []

	# 	num_of_intersection = int(sf.readline())
	# 	num_of_intersection = int(sf.readline())

	# 	for intersection in range(num_of_intersection):
	# 		for street_name in
	# 		street_name, duration_str = sf.readline().split()


	# 		librarys_selected_with_books.append(
	# 			LibraryBooksTuple(
	# 				librarys[lib_id],
	# 				# finding corresponding books obj to represent in the sumbit info
	# 				books_ids_to_books(books_ids, librarys[lib_id].books)))

	# return SubmitInfo(librarys_selected_with_books)