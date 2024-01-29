def main():
    print("Enter the number:")
    no=int(input())

    print(f"Multiplication table of {no} is:")
    i=1
    while i<=10:
        print(no*i)
        i=i+1


if __name__ == "__main__":
    main()