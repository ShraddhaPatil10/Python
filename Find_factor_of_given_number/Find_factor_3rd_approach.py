def main():
    print("Enter the number:")
    no=int(input())

    i=1
    print("Factors are:")
    while(i<int(no/2)+1):
        if no%i==0:
            print(i)

        i=i+1

if __name__=="__main__":
    main()