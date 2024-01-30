def main():
    print("How many numbers addition do you want?")
    n=int(input())

    res=Rec(n)
    print(f"Addition of {n} natural numbers is:{res}")

def Rec(n):
    if n<=1:
        return n
    else:
        return n+Rec(n-1)


if __name__=="__main__":
    main()