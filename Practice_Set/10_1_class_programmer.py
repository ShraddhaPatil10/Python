class Programmer:
    company="Microsoft"
    def __init__(self):
        self.name=""
        self.salary=0

    def Accept(self):
        print("How many employees information do you want to fill:")
        self.size=int(input())
        for i in range(0,self.size,1):
            print(f"Enter name of {i+1} employee:")
            self.name=input()

            print(f"Enter salary of {i+1} employee:")
            self.salary=int(input())

    def Display(self):
        for i in range(0,self.size,1):
            print(f"{i+1} employee name:{self.name}")
            print(f"{i+1} employee salary:{self.salary}")
            print(f"Company name is:{Programmer.company}\n\n")


def main():
    obj=Programmer()

    obj.Accept()
    obj.Display()


if __name__=="__main__":
    main()