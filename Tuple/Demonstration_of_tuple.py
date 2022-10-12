def main():
    print("Demonstration of Tuple")

    #Characteristics of Tuple
    #data:Hetrogeneous
    #ordered:Yes
    #Indexed:Yes
    #Mutable:No
    #Duplicate:Yes

    data=(11,21,51,101,21,11)            #Allows Duplicates
    data1=(10,12.35,True,"Hello")        #Hetrogeneous

    print("*****************************************")

    print("Data is hetrogeneous:",data1)
    print("Data is ordered:",data1)
    print("Data at index 2 is:",data1[2])
    print("Data allows duplicates:",data)

    print("**************************************")

if __name__=="__main__":
    main()