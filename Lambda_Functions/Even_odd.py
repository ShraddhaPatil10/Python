def ChcekEven(no):
    if no%2==0:
        return True
    else:
        return False

def CheckEven1(no):
    return (no%2==0)

Even = lambda no : no%2==0

#Res=CheckEven(12)
#Res=CheckEven1(12)
Res=Even(12)

if (Res==True):
    print("Its Even")

else:
    print("Its Odd")