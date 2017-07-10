import json

class People(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

#json serialize
def serialize_instance(obj):
    d = { '__classname__' : type(obj).__name__ }
    d.update(vars(obj))
    return d

# Dictionary mapping names to known classes
classes = {
    'People' : People
}

#json deserialize
def deserialize_object(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls) # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
        return obj
    else:
        return d

def write_as_string(obj):
    return json.dumps(obj, default=serialize_instance, indent=2)

def read_from_string(str_json):
    return json.loads(str_json, object_hook=deserialize_object)


filePath = __file__
# indent is a format param
peopleJson = json.dumps(People("wang", 22),default=serialize_instance, indent=2)

# print(peopleJson)
# print(write_as_string(People("wang", 22)))

print(json.loads(peopleJson, object_hook=deserialize_object))