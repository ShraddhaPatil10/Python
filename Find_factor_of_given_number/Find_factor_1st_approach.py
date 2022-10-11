def main():
    print("Enter the number:")
    num=int(input())
    
    print("Factors are:")
    for i in range(1,num+1,1):
        if num%i==0:
            print(i)

if __name__=="__main__":
    main()