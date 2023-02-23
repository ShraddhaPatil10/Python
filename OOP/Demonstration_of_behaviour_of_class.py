print("Demonstration of behaviour of class")

class Demo:
    def __init__(self):
        self.i=0
        self.j=0

    def fun(self):
        print("Inside instance")

    @classmethod
    def gun(cls):
        print("Inside clss method")

    @staticmethod
    def sun():
        print("Inside static")

def main():
    obj1=Demo()
    obj1.fun()
    Demo.gun()
    Demo.sun()

if __name__=="__main__":
    main()