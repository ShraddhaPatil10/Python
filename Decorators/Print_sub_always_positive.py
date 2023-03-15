def Subtraction(no1,no2):
    Ans=0
    Ans=no1-no2
    return Ans

def Decorated_Function(Function_name):
    def Inner(A,B):
        if(A<B):
            A,B=B,A
        Output=Function_name(A,B)
        return Output

    return Inner

def main():
    val1=int(input("Enter 1st number:"))
    val2=int(input("Enter 2nd number:"))

    New_Function=Decorated_Function(Subtraction)
    ret=New_Function(val1,val2)
    print("Subtraction is:",ret)

if __name__=="__main__":
    main()