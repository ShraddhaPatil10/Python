#Pass fun as parameter to another function
def Demo():
    print("Inside Demo")

def Fun():
    print("Inside fun")

def Hello(FPTR):
    print("Inside Hello")
    FPTR()

Hello(Demo)
Hello(Fun)
#Hello(11)    --> Not Allowed