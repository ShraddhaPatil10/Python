def main():
    print("Enter 1st number:")
    no1=int(input())

    print("Enter 2nd number:")
    no2=int(input())

    if no1>no2:
        print(f"{no1} is greater than {no2}")
    else:
        print(f"{no2} is greater than {no1}")

if __name__=="__main__":
    main()