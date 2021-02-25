from intersection import Intersection
from car import Car
from flow_chart import CarStatus, InitialFlowRet
from street import Street

initialFlowRet = get_initial_flow()

def weightByMoreCars(carsStatuses: dict, timeForEnd:list):

def weightByLessTime(carsEnriesTime: list, timeForEnd:list):

def streetAverage(timeForEnd:list):
    average = 0
    for car in timeForEnd:
        average += timeForEnd[car]
    average = average / len(timeForEnd.keys())

# run for each intersaction
def changeWeight(intersections: List[Intersection], initialiFlowRet: InitialFlowRet, streetWithSchedule: list):
    resultList = []
    for intersection in intersections:
        resultList.append(chooseWeightForRoadInIntersection(intersection, InitialFlowRet, streetWithSchedule))
    return resultList

def chooseWeightForRoadInIntersection(intersection: Intersection, initialiFlowRet: InitialFlowRet, streetWithSchedule: list) -> IntersectionWithSchedule:
    averageStreet = {}
    resultIntersactionWithSchedule = intersactionWithSchedule
    for Road in intersection.in_streets:
        endCarTime = {}
        for car in initialiFlowRet.car_street_times[Road].keys():
            endCarTime[car] = initialiFlowRet.car_end_times[car] - initialiFlowRet.car_street_times[Road][car]
        averageStreet[Road] = streetAverage(endCarTime)

    max = -1
    min = 10000000000000000000000000
    for value in averageStreet.values():
        if max < value:
            max = value
        if mix > value:
            min = value

    
    for Road in averageStreet:
        streetWithSchedule.duration = math.ceil(max/Road*streetWithSchedule.duration)

    return streetWithSchedule