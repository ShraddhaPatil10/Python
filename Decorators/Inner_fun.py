def Hello():
    print("Inside Hello")

    def Demo():
        print("Inside Demo")

    Demo()

Hello()
#Demo()    ---> We cannot call inner fun from outside