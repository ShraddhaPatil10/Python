def Add(A,B):
    return A+B

def Sub(A,B):
    return A-B

def Calculator(Target,val1,val2):
    return Target(val1,val2)

Ret=Calculator(Target=Add,val1=10,val2=20)
print("Addition is:",Ret)

Ret=Calculator(Target=Sub,val1=20,val2=10)
print("Subtraction is:",Ret)