def main():
    f=open("Multiplication_Table","w")

    print("Enter the number to print multiplication table:")
    no=int(input())

    for i in range(1,11,1):
        mul=no*i
        f.write(str(mul))

    f.close()


if __name__=="__main__":
    main()