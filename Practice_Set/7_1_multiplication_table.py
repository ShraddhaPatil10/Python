def main():
    print("Enter the number:")
    no=int(input())

    print(f"Multiplication table of {no} is:")
    for i in range(1,11,1):
        print(no*i)

if __name__=="__main__":
    main()