import json

def serialize_instance(obj):
    return vars(obj)

class Tree:
    # define the struct
    def __init__(self, value):
        self.value = value
        self.children = []

    # repr() is default method toString()
    def __repr__(self):
        return str(self.value)

    # convert to json
    def toJson(self):
        return json.dumps(self, default=serialize_instance, indent=2)

    def __add__(self, children):
        self.children.append(children)

    # implements default iter
    def __iter__(self):
        return iter(self.children)

    # deepinly iterate first
    def depth_first(self):
        yield self
        for i in self:
            yield from i.depth_first()


root = Tree(0)
nodeF10 = Tree(10)
nodeF11 = Tree(11)
nodeF21 = Tree(21)
nodeF22 = Tree(22)
nodeF23 = Tree(23)

root.__add__(nodeF10)
root.__add__(nodeF11)
nodeF10.__add__(nodeF21)
nodeF10.__add__(nodeF22)
nodeF11.__add__(nodeF23)

print(root.toJson())

print("print by iter")
for node in root.depth_first():
    print(node)
