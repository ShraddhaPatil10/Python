def Mult(no):
    print("Multiplication table is:")
    for i in range(1,11,1):
        print(no*i)

def main():
    print("Enter the number:")
    no=int(input())

    Mult(no)

if __name__=="__main__":
    main()