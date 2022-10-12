def main():
    print("Demonstration of set")

    #Characteristics of set
    #data:Hetrogeneous
    #ordered:No
    #Indexed:No
    #Mutable:Yes
    #Duplicates:No

    data={11,21,51,101,11,21}
    data1={10,12.35,True,"Hello"}

    print("First set data:",data)
    print("Length of data:",len(data))
    print("Data is hetrogeneous:",data1)
    print("Data is not ordered:",data1)
    #print("Data at index 2 is:",data1[2])
    print("Data with unique elements:",data)

    print("Set is mutable")
    #Insert element in set
    data.add(211)
    print("Data after insertion:",data)

    #Remove Element
    data.remove(211)
    print("Data after removel:",data)

    #data.remove(201)
    data.discard(201)
    print("Data after discard:",data)

if __name__=="__main__":
    main()