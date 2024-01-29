def main():
    print("Enter the number:")
    no=int(input())

    fact=1
    for i in range(1,no+1,1):
        fact=fact*i

    print(f"Factorial of {no} is: {fact}")


if __name__ == "__main__":
    main()