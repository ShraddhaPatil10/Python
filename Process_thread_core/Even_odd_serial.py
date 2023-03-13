def DisplayEven(no):
    for i in range(no):
        if(i%2==0):
            print("Even number:",i)

def DisplayOdd(no):
    for i in range(no):
        if(i%2!=0):
            print("Odd number:",i)

def main():
    print("Demonstration of serial programming")

    DisplayEven(2000)
    DisplayOdd(2000)

if __name__=="__main__":
    main()
