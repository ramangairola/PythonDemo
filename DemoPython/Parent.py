class ParentClass:
    num = 100

    def __init__(self, a, b):
        self.firstValue = a
        self.secondValue = b
        print("This is a param constructor")

    def val(self):
        print("This is a method")

    def getdata(self):
        return self.firstValue + self.secondValue + self.num


def fun():
    obj = ParentClass(2, 3)
    obj.val()
    print(obj.getdata())


fun()

