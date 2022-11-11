def CheckEven(no):
    return (no%2==0)

def Multiply(no):
    return no*2

def sum(A,B):
    return A+B

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
    print("How many elements do you want to enter in list:")
    isize=int(input())

    data_input=[]
    print("Enter the list elements:")
    for i in range(0,isize,1):
        value=int(input())
        data_input.append(value)

    print("Data is:",data_input)

    data_filter=filterx(CheckEven,data_input)
    print("Data after filter is:",data_filter)

    data_map=mapx(Multiply,data_filter)
    print("Data after map:",data_map)

    output=reducex(sum,data_map)
    print("Data after reduce is:",output)

if __name__=="__main__":
    main()
