def main():
    no1 = int(input("Enter 1st number:"))
    no2 = int(input("Enter 2nd number:"))
    no3 = int(input("Enter 3rd number:"))
    no4 = int(input("Enter 4th number:"))

    if no1>no2:
        max1=no1
    else:
        max1=no2

    if no3>no4:
        max2=no3
    else:
        max2=no4

    if max1>max2:
        print(f"Maximum number is:{max1}")
    else:
        print(f"Maximum number is:{max2}")

if __name__=="__main__":
    main()