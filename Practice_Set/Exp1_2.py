#Arithmetic Operators
def main():
    print("Enter 1st number:")
    no1=int(input())

    print("Enter 2nd number:")
    no2=int(input())

    sum=no1+no2
    print("Addition of",no1,"and",no2,"is:",sum)

    sub=no1-no2
    print("Subtraction of",no1,"and",no2,"is:",sub)

    Mul=no1*no2
    print("Multiplication of",no1,"and",no2,"is:",Mul)

    Div=no1/no2
    print("Division of",no1,"and",no2,"is:",Div)

    Mod=no1%no2
    print("Mod of",no1,"and",no2,"is:",Mod)

    Flour_div=no1//no2
    print("Flour division of",no1,"and",no2,"is:",Flour_div)

    pow=no1**no2
    print(no1,"^",no2,"is:",pow)


if __name__=="__main__":
    main()