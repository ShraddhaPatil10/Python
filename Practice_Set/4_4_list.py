def main():
    l1=[]
    print("How many elements do you want to enter:")
    size=int(input())

    for i in range(0,size,1):
        print(f"Enter element no {i+1}:")
        val=int(input())
        l1.append(val)

    print("Sum of all elements in list:",sum(l1))

if __name__=="__main__":
    main()