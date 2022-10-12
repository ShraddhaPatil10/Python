def main():
    programming={"PPA":18000,"LB":18500,"Python":16500,"Angular":15000}

    Batches={"PPA":18000,"LB":18500,"Python":16500,"Angular":15000}

    print("Data traversal using for loop")
    for x in Batches:
        print(x)        #It will displays key only

    print("*******************************************")

    print("Data traversal using for loop")
    for x in Batches:
        print(x,Batches[x])     #It will displays keys and values also

    print("*********************************************")

    print("Data traversal using for loop")
    for x in Batches:
        print(x,Batches.get(x))

    print("*********************************")
    keyBatches=Batches.keys()
    print(keyBatches)
    print(type(keyBatches))

    print("*********************************")
    valueBatches=Batches.values()
    print(valueBatches)
    print(type(valueBatches))

    print("**********************************")
    
if __name__=="__main__":
    main()