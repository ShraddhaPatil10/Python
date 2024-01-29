def main():
    print("How many numbers addition do you want:")
    size=int(input())

    sum=0
    for i in range(0,size+1,1):
        sum=sum+i

    print(f"Addition of first {size} numbers is:",sum)


if __name__ == "__main__":
    main()