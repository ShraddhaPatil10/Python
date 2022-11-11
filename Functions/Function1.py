#Fun which accepts nothing and returns nothing
def demo1():
    print("Inside demo1")

#Fun which accepts one parameter and returns nothing
def demo2(no):
    print("Inside demo2 with argument:",no)

#Fun which accepts one parameter and return one parameter
def demo3(no):
    print("Inside demo3 with argument:",no)
    return no+2

#Fun which accepts two parameters and return one parameter
def demo4(no1,no2):
    print("Inside demo4")
    Add=no1+no2
    return Add

#Fun which accepts two parameters and return two parametrs
def demo5(no1,no2):
    print("Inside demo5")
    Add=no1+no2
    Sub=no1-no2
    return Add,Sub

def main():
    demo1()

    demo2(11)

    Ans=demo3(10)
    print("Return value from demo3 is:",Ans)

    Ans=demo4(10,11)
    print("Return value from demo4 is:",Ans)

    Ans1,Ans2=demo5(11,10)
    print("Addition is:",Ans1)
    print("Substraction is:",Ans2)

if __name__=="__main__":
    main()