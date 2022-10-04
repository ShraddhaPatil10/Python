print("Application To Demonstrate Industrial Application")

def Addition(value1,value2):
    Ans=value1+value2
    return Ans

def main():
    print("Enter 1st number:")
    no1=input()

    print("Enter 2nd number:")
    no2=input()

    Ans=Addition(int(no1),int(no2))

    print("Addition is:",Ans)

if __name__=="__main__":
    main()