from snip.JsonObject import write_as_string
from snip.JsonObject import read_from_string
class ObjA(object):
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.attribute3 = []
        self.attribute4 = {}

    def __setAttr3__(self, value):
        self.attribute3 = value

insObjA = ObjA(123,"abc")
print(write_as_string(insObjA))
insObjA.__setAttr3__([1,2,"aa","bb"])
print(write_as_string(insObjA))
insObjA.__setattr__("attribute5","test5")
print(write_as_string(insObjA))
print(read_from_string(write_as_string(insObjA)))
