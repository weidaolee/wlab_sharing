import abc
from multipledispatch import dispatch
from collections import Iterable


class DrawingObject(metaclass=abc.ABCMeta):

    def __init__(self, idx):
        self.idx = idx

    @abc.abstractmethod
    def show(self): ...


class Text(DrawingObject):
    def __init__(self, idx):
        super(Text, self).__init__(idx)

    def show(self):
        print(f"Text Object {self.idx}")


class Geo(DrawingObject):
    def __init__(self, idx):
        super(Geo, self).__init__(idx)

    def show(self):
        print(f"Geo Object {self.idx}")


class Group(DrawingObject):
    def __init__(self, idx):
        super(Group, self).__init__(idx)

        self.groups = []

    @dispatch(DrawingObject)
    def add(self, obj):
        self.groups.append(obj)

    @dispatch(Iterable)
    def add(self, objs):
        for o in objs:
            self.groups.append(o)

    def show(self):
        print(f"Group Object {self.idx}")
        for o in self.groups:
            o.show()

t = {k: Text(k) for k in range(5)}
g = {k: Geo(k) for k in range(5)}

group_0 = Group(0)
group_1 = Group(1)

for i in range(5):
    group_0.add(t[i])

group_0.add([g[i] for i in range(5)])

group_0.add(group_1)

group_0.show()


