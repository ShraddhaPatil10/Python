def Square(No):
    return (No*No)

def main():
    data=[1,2,3,4,5]

    Result=[]
    for value in data:
        Result.append(Square(value))

    print("Result after aquare operation is:",Result)

if __name__=="__main__":
    main()