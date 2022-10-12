def main():
    Arr=list()

    print("Enter how many numbers do you want to add:")
    size=int(input())

    print("Enter the elements:")
    for i in range(0,size):
        no=int(input())
        Arr.append(no)

    print(Arr)

if __name__=="__main__":
    main()