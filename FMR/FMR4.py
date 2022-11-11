from functools import reduce

def main():
    print("How many numbers do you want to enter:")
    isize=int(input())

    data_input=[]
    print("Enter the elements:")
    for i in range(0,isize,1):
        values=int(input())
        data_input.append(values)

    print("Given data is:",data_input)

    data_filter=list(filter(lambda no : no%2==0,data_input))
    print("Data after filter:",data_filter)

    data_map=list(map(lambda no : no*2,data_filter))
    print("Data after map:",data_map)

    output=reduce(lambda A,B : A+B,data_map)
    print("Data after reduce:",output)

if __name__=="__main__":
    main()