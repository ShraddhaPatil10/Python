def main():
    print("Enter the temperature in celsius:")
    temp=int(input())

    fah=int((9/5*temp)+32)

    print(f"Temperature in fahrenheit is {fah}")

if __name__=="__main__":
    main()