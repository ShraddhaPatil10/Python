def Sumfactor(no):
    sum=0
    for i in range(1,int(no/2)+1,1):
        if no%i==0:
            sum=sum+i

    return sum

def Prime(no):
    Res=Sumfactor(no)

    if Res==1:
        return True
    else:
        return False

def main():
    print("Enter the number:")
    no=int(input())

    Res=Prime(no)

    if Res==True:
        print(f"Given number {no} is prime")
    else:
        print(f"Given number {no} is not prime")


if __name__ == "__main__":
    main()