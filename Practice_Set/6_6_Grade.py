def main():
    print("Enter your marks:")
    marks=int(input())

    if marks>=90 and marks<=100:
        print("Ex")
    elif marks>=80 and marks<90:
        print("A")
    elif marks>=70 and marks<80:
        print("B")
    elif marks >= 60 and marks<70:
        print("C")
    elif marks >= 60 and marks < 70:
        print("D")
    elif marks<=50:
        print("Fail")
    else:
        print("Enter correct marks!!!")

if __name__=="__main__":
    main()