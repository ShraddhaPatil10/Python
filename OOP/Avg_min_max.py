class Numbers:
    def __init__(self):
        self.Arr=list()
        self.size=0

    def Accept(self):
        print("How many elements do you want:")
        self.size=int(input())

        print("Please enter the elements:")
        for i in range(0,self.size,1):
            val=int(input())
            self.Arr.append(val)

    def Display(self):
        print("Elements in list are:")
        for i in range(0,self.size,1):
            print(self.Arr[i])

    def Average(self):
        sum=0
        for i in range(0,self.size,1):
            sum=sum+self.Arr[i]

        return(sum/self.size)

    def Max(self):
        max=self.Arr[0]
        for i in range(0,self.size,1):
            if(max<self.Arr[i]):
                max=self.Arr[i]

        return max

    def Min(self):
        min=self.Arr[0]
        for i in range(0,self.size,1):
            if min>self.Arr[i]:
                min=self.Arr[i]

        return min

def main():
    obj=Numbers()
    obj.Accept()
    obj.Display()

    output=obj.Average()
    print("Average of all elements:",output)

    output=obj.Max()
    print("Maximum number from list is:",output)

    output=obj.Min()
    print("Minimum number from list is:",output)

if __name__=="__main__":
    main()