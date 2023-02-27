class Arithmetic:
    def __init__(self,A,B):
        print("Inside init method")
        self.no1=A
        self.no2=B

    def Add(self):
        Ans=self.no1+self.no2
        return Ans

    def Sub(self):
        Ans=self.no1-self.no2
        return Ans

def main():
    print("Inside main method")
    obj=Arithmetic(11,10)

    output=obj.Add()
    print("Addition is:",output)

    output=obj.Sub()
    print("Substraction is:",output)

    objx=Arithmetic(50,10)

if __name__=="__main__":
    main()