class Numbers:
    def __init__(self):
        self.size=0
        self.Arr=list()
        self.Accept()

    def Accept(self):
        print("Enter how many elements do you want:")
        self.size=int(input())

        print("Please enter elements you want:")
        val=0
        for i in range(0,self.size,1):
            val=int(input())
            self.Arr.append(val)

    def Display(self):
        print("Elements from list are:")
        for i in range(0,self.size,1):
            print(self.Arr[i])

    def Summation(self):
        sum=0
        for i in range(0,self.size,1):
            sum=sum+self.Arr[i]

        return sum

    def Average(self):
        sum=0
        for i in range(0,self.size,1):
            sum=sum+self.Arr[i]

        return (sum/self.size)

    def CheckPrime(self,no):
        i=0
        Flag=True
        for i in range(2,int(no/2)+1):
            if(no%i==0):
                Flag=False
                break

        return Flag

    def Display_Factor(self):
        for i in range(0,self.size,1):
            if(self.CheckPrime(self.Arr[i])==True):
                print("{} is a prime number".format(self.Arr[i]))

def main():
    obj=Numbers()
    obj.Display()

    output=obj.Summation()
    print("Summation of all elements is:",output)

    output=obj.Average()
    print("Average of all elements is:",output)

    obj.Display_Factor()

if __name__=="__main__":
    main()


