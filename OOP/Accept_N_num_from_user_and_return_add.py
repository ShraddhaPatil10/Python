class Numbers:
    def __init__(self):
        self.arr=list()
        self.size=0

    def Accept(self):
        print("Enter how many elements you want:")
        self.size=int(input())

        print("Please enter the elements")
        value=0
        for i in range(0,self.size,1):
            val=int(input())
            self.arr.append(val)

    def Display(self):
        print("Elements in list are:")
        for i in range(0,self.size,1):
            print(self.arr[i])

    def Summation(self):
        sum=0
        for i in range(0,self.size,1):
            sum=sum+self.arr[i]

        return sum

def main():
    obj=Numbers()
    obj.Accept()
    obj.Display()
    output=obj.Summation()
    print("Summation of all elements:",output)

if __name__=="__main__":
    main()