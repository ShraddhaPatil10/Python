def Add(no1,no2):
    print("Value of no1:",no1)
    print("Value of no2:",no2)
    return no1+no2

def Sub(no1,no2):
    print("Value of no1:",no1)
    print("Value of no2:",no2)
    return no1-no2

def main():
    Ans=0
    Ans=Add(11,10)
    print("Addition is:",Ans)

    Ans=Sub(11,10)
    print("Substraction is:",Ans)

if __name__=="__main__":
    main()
