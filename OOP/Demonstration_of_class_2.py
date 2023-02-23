print("Demonstration of class")

class Demo:
    x=10
    def __init__(self,no1,no2):
        self.i=no1
        self.j=no2

def main():
    obj1=Demo(10,20)
    obj2=Demo(11,10)

    print(obj1.i)
    print(obj1.j)

    print(obj2.i)
    print(obj2.j)

    print(Demo.x)

if __name__=="__main__":
    main()