def main():
    print("Demonstration of dictionary")

    #Characteristics of dictionary
    #data:Hetrogeneous
    #ordered:Yes
    #Indexed:No
    #Mutable:Yes
    #Duplicates:No

    programming={"C":"Ritche","C++":"Strostrup","Java":"Gosling","Python":"Rossum","C":"Thomsan"}

    Batches={"PPA":18000,"LB":18500,"Python":16500,"Angular":15000}

    print("Data of dictionary:",Batches)
    print("Data type is:",type(Batches))
    print("Length of dictionary:",len(Batches))

    print("Value of PPA:",Batches["PPA"])

    print(programming)

if __name__=="__main__":
    main()
