import math
class Calculator:
    def __init__(self,no):
        self.no=no

    def Square(self):
        return self.no*self.no

    def Cube(self):
        return self.no*self.no*self.no

    def Square_Root(self):
        return math.sqrt(self.no)

def main():
    print("WELCOME TO SHRADDHA'S CALCULATOR!!!!")

    print("Enter the number:")
    no=int(input())

    print("Enter your choice:\n1.Square\n2.Cube\n3.Square Root\n4.All operations")
    choice=int(input())

    obj=Calculator(no)

    if choice==1:
        res=obj.Square()
        print(f"Square of {no} is:",res)

    elif choice==2:
        res=obj.Cube()
        print(f"Cube of {no} is:",res)

    elif choice==3:
        res=obj.Square_Root()
        print(f"Square root of {no} is:",res)

    elif choice==4:
        res1=obj.Square()
        print(f"Square of {no} is:", res1)

        res2=obj.Cube()
        print(f"Cube of {no} is:", res2)

        res3=obj.Square_Root()
        print(f"Square root of {no} is:", res3)

    else:
        print("Enter proper choice")

if __name__=="__main__":
    main()