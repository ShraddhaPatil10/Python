def main():
    l1=[]
    for i in range(0,3,1):
        print(f"Enter the marks of sub{i+1}:")
        marks=int(input())
        l1.append(marks)

    if sum(l1)/3>=40:
        print("You are Pass!!!")
    else:
        print("You are fail!!!")

if __name__=="__main__":
    main()