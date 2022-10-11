def factor(num):
    i=1
    print("Factors are:")
    while(i<=int(num/2)):
        if num%i==0:
            print(i)

        i+=1

def main():
    print("Enter the number:")
    no=int(input())

    factor(no)

if __name__=="__main__":
    main()