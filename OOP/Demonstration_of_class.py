print("Demonstration of class")

class demo:
    def __init__(self,val1,val2):
        print("Inside init method")
        self.i=val1
        self.j=val2

    def fun(self):
        print("Inside fun")
        print(self.i,self.j)

    def Add(self):
        print("Addition is:",self.i+self.j)

def main():
    #create object of demo class
    obj1=demo(10,20)

    #call the method function
    obj1.fun()

    #create object of demo class
    obj2=demo(30,50)

    #call the method fun
    obj2.fun()

    #call the method Add to perform addition
    obj1.Add()
    obj2.Add()

if __name__=="__main__":
    main()