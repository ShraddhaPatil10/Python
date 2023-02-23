print("Demonstration of advanced functions")
#fun which accepts nothing and return nothnig
def Marvellous1():
    print("Inside Marvellous1")

#fun which accepts value and return nothing
def Marvellous2(val):
    print("Inside Marvellous2")
    print("Accepted value is:",val)

#fun which accepts value and return value
def Marvellous3(val):
    print("Inside Marvellous3")
    print("Accepted value is:",val)
    return val+1


# fun which accepts multiple values and return multiple values
def Marvellous4(val1,val2):
    print("Inside Marvellous4")
    add=val1+val2
    sub=val1-val2
    return add,sub

#Fun which calls another fun which is defined inside outside it
def Marvellous5():
    print("Inside Marvellous5")
    Marvellous1()

#Fun which contains another nested function defined in it
def Marvellous6():
    print("Inside Marvellous6")
    def Innerfun():
        print("Inside Innerfun")

    Innerfun()

#Fun calls for above functions
no=11
Marvellous1()
Marvellous2(no)

Ret=Marvellous3(no)
print("Return value is:",Ret)

Marvellous5()
ret1,ret2=Marvellous4(10,4)
print("Addition is:",ret1)
print("Substraction is:",ret2)
