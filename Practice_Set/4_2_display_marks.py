def main():
    print("Enter the marks:")
    l1=[]
    for i in range(0,6,1):
        print(f"Enter marks of student no {i+1}:")
        marks=int(input())
        l1.append(marks)

    l1.sort()
    print(l1)
    
if __name__=="__main__":
    main()