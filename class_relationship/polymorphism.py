import abc

class IFlyable(metaclass=abc.ABCMeta):
    def __init__(self): ...

    @abc.abstractmethod
    def fly(self): ...


class Bird(IFlyable):
    def __init__(self):
        ...

    def fly(self):
        print("Bird fly")


class Rocket(IFlyable):
    def __init__(self):
        ...

    def fly(self):
        print("Rocket fly")


bird = Bird()
rocket = Rocket()

a_list = [bird, rocket]

for o in a_list:
    if isinstance(IFlyable):
        o.fly()
