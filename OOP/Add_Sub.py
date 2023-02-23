#Accept 2 numbers from user and perform addition & substraction

class Arithmetic:
    def __init__(self,A,B):
        self.no1=A
        self.no2=B

    def Add(self):
        return self.no1+self.no2

    def Sub(self):
        return self.no1-self.no2

def main():
    print("Enter 1st number:")
    num1=int(input())

    print("Enter 2nd number:")
    num2=int(input())

    obj=Arithmetic(num1,num2)

    Ans=obj.Add()
    print("Addition is:",Ans)

    Ans=obj.Sub()
    print("Substraction is:",Ans)

if __name__=="__main__":
    main()