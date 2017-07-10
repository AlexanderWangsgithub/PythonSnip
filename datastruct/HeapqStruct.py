import heapq
import json

from pprint import pprint

ages = [18, 34, 24, 90, 17, 54, 43, 23]


class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# json serialize
def serialize_instance(obj):
    d = vars(obj)
    return d


peopleList = [
    People("wang", 22),
    People("san", 35),
    People("zhang", 18),
    People("gang", 23)
]

pprint(peopleList)

minAge = heapq.nsmallest(2, peopleList, key=lambda p: p.age)
maxAge = heapq.nlargest(1, peopleList, key=lambda p: p.age)
print("minAge:")
print(json.dumps(minAge, default=serialize_instance))
print("maxAge:")
print(json.dumps(maxAge, default=serialize_instance))
