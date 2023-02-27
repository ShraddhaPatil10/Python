class Value:
    def __init__(self,data):
        self.no=data

    def Sumfactor(self):
        sum=0
        for i in range(1,int(self.no/2)+1,1):
            if(self.no%i==0):
                sum=sum+i

        return sum

    def Check_Prime(self):
        Ans=self.Sumfactor()

        if(Ans==1):
            return True
        else:
            return False

    def Check_Perfect(self):
        Ans=self.Sumfactor()
        
        if(self.no==Ans):
            return True
        else:
            return False


def main():
    print("Enter the number:")
    num=int(input())

    obj=Value(num)

    Res=obj.Sumfactor()

    Res=obj.Check_Prime()
    if(Res==True):
        print("{} is a prime number".format(num))

    else:
        print("{} is not a prime number".format(num))

    Res=obj.Check_Perfect()
    if(Res==True):
        print("{} is a perfect number".format(num))

    else:
        print("{} is not a perfect number".format(num))

if __name__=="__main__":
    main()