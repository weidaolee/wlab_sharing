class A:
    def __init__(self, a, x):
        self.a = a
        self.x = x


class B:
    def __init__(self):
        self.b = 0
        self.x = 'x'


class C(A, B):
    def __init__(self, a, x):
        super(C, self).__init__(a, x)


c = C(a=0, x=2)
