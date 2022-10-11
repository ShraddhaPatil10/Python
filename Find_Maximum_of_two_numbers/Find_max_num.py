def Max(value1,value2):
    if value1>value2:
        return value1
    else:
        return value2

def main():
    print("Enter 1st number:")
    num1=int(input())

    print("Enter 2nd number:")
    num2=int(input())

    Res=Max(num1,num2)

    print("Maximum number is:",Res)

if __name__=="__main__":
    main()