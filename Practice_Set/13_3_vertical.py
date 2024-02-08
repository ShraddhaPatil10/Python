def main():
    print("Enter the number:")
    no=int(input())

    mult_table=[no*i for i in range(1,11)]

    print("\n".join(map(str,mult_table)))

if __name__=="__main__":
    main()