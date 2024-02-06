def main():
    print("Enter the number:")
    no=int(input())

    mult_table=[no*i for i in range(1,11)]

    with open("file.txt",'w') as f:
        f.write(f"Table of {no}:")
        f.write(str(mult_table))


if __name__=="__main__":
    main()