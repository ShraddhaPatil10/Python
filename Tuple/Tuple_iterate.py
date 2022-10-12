def main():
    print("Tuple Iterate")

    data=(11,21,51,101)

    print("Output using for loop:")
    for no in data:
        print(no,end=" ")

    print("\n****************************************")

    print("Output using for loop with index:")
    for i in range(0,len(data)):
        print(data[i],end=" ")

    print("\n*******************************************")

    print("Output using while loop:")
    i=0
    while i<len(data):

    print("\n**************************************************
        print(data[i],end=" ")
        i+=1

if __name__=="__main__":
    main()