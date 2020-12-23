class Person:
    def __init__(self, name):
        self.name = name
        self.marriage = None

    def get_marry(self, person):
        if person.marriage is None:
            self.marriage = Marriage()
            self.marriage.add_person(self)
            self.marriage.add_person(person)

        else:
            self.marriage = person.marriage
            self.marriage.add_person(self)


class Marriage:
    def __init__(self):
        self.people = set()

    def add_person(self, person):
        self.people.add(person)


a = Person('a')
b = Person('b')

a.get_marry(b)

c = Person('c')
c.get_marry(a)
