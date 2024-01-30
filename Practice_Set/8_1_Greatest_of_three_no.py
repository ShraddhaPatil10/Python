def main():
    print("Enter 1st no:")
    no1=int(input())

    print("Enter 2nd no:")
    no2=int(input())

    print("Enter 3rd no:")
    no3=int(input())

    if no1>no2:
        max=no1
    else:
        max=no2

    if no3>max:
        greatest=no3
    else:
        greatest=max

    print("Greatest number is:",greatest)

if __name__=="__main__":
    main()