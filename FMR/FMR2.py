CheckEven = lambda no : no%2==0

Multiply = lambda no : no*2

sum = lambda A,B : A+B

def filterx(Helper_fun,data):
    Result=[]
    for no in data:
        if(Helper_fun(no)==True):
            Result.append(no)

    return Result

def mapx(Helper_fun,data):
    Result=[]
    for no in data:
        values=Helper_fun(no)
        Result.append(values)

    return Result

def reducex(Helper_fun,data):
    Ans=0
    for no in data:
        Ans=Helper_fun(Ans,no)

    return Ans

def main():
    print("How many numbers do you want to enter:")
    isize=int(input())

    Data_input=[]
    print("Enter the elements in list:")
    for i in range(0,isize,1):
        value=int(input())
        Data_input.append(value)

    print("Given data is:",Data_input)

    data_filter=filterx(CheckEven,Data_input)
    print("Data after filter:",data_filter)

    data_map=mapx(Multiply,data_filter)
    print("Data after map is:",data_map)

    output=reducex(sum,data_map)
    print("Data after reduce:",output)

if __name__=="__main__":
    main()