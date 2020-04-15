class a:

    o = b()
    o.b

    def aMethod(self):
        print("A")


class b:
    def bMethod(self):
        print("B")


obj = a()
obj.aMethod();
