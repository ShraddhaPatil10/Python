def main():
    print("Enter the no:")
    no=int(input())

    i=10
    print(f"Reverse multiplication table of {no} is:")
    while i>=1:
        print(i*no)
        i=i-1

if __name__=="__main__":
    main()