# hook object test

import json

class Order(object):
    def __init__(self, food, fee):
        self.food = food
        self.fee = fee

    def toString(self):
        return "food = " + str(self.food) + " fee = " + str(self.fee)


params = '''{
        "food":"potatoes",
        "fee":10
    }'''


# The func json.loads return Dict, every element of the Dict was Tuple
# This struct keep the sequence of origin json, but also bring some inconvenient
def jsonToObj(dictJson):
    print("dictJson type : " + str(type(dictJson)))
    print("dictJson : " + str(dictJson))
    return Order(tuple(dictJson[0])[1], tuple(dictJson[1])[1])


# object_pairs_hook is a func to inject the func to convert json_to_dict to object.
order = json.loads(params, object_pairs_hook=jsonToObj)

print("order : " + str(order))

# We can summary that, functions in Python are static.
# So, we just put the object pointer to func.
print(order.toString)
print(order.toString())
print(Order.toString(order))
