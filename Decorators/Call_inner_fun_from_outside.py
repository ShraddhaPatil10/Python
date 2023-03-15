#Call inner fun from outside
def Outer():
    print("Inside Outer")

    def Inner():
        print("Inside inner")

    print(id(Inner))

    return Inner

Ret=Outer()
print(type(Ret))
print("ID:",id(Ret))
Ret()