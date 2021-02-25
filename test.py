# this file should use you for free testing dont upload it. play with it

from car import Car
from street import Street
from submit import SubmitInfo
from inputparser import get_input

file_path = "data-sets/a.txt"

def main():
	print("Started running ...")
	ic = get_input(file_path)
	print(ic)
	import IPython
	IPython.embed()


if __name__ == '__main__':
	main()
