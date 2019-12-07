class Test:
    def __init__(self, a = 0):
        self.a = a

    def hallo(self):
        print("Hallo")

class AnakTest(Test):
    def __init__(self, a, b):
        super().__init__(a)
        self.b = b

x = AnakTest(1, 2)
print(x.a)
x.hallo()

