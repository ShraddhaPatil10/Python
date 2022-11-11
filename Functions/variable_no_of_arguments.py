def Add(*values):
    sum=0
    for i in values:
        sum=sum+i

    return sum

def Mul(*values):
    mul=1
    for i in range(0,len(values),1):
        mul=mul*values[i]

    return mul

def main():
    Ans=Add(11,10,3,40)
    print("Addition is:",Ans)

    Ans=Mul(2,3,4,1)
    print("Multiplication is:",Ans)

if __name__=="__main__":
    main()