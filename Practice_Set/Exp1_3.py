#Create,Concatenate and print a string

def main():
    print("Enter 1st string:")
    str1=input()

    print("Enter 2nd string:")
    str2=input()
    print("")

    #1st approach
    print(str1,str2)
    print("")

    #2nd approach
    print(str1 + str2)
    print("")

    #3rd approach
    str="{} {}".format(str1,str2)
    print(str)
    print("")

    #4th approach
    str.join([str1,str2])
    print(str)
    print("")

    #5th approach
    print(f"{str1}{str2}")


if __name__=="__main__":
    main()