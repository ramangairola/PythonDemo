from DemoPython.Parent import ParentClass


class ChildClass(ParentClass):
    num2 = 100

    def __init__(self):
        ParentClass.__init__(self, 2, 4)

    def childmethod(self):
        print(self.num2 + self.getdata())
        print("Git basic commands")


obj = ChildClass()
obj.childmethod()
