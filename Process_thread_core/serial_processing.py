def Square(n):
    return(n*n)

if __name__=="__main__":
    arr=[1,2,3,4,5]

    result=[]

    for num in arr:
        result.append(Square(num))

    print(result)