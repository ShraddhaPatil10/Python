def main():
    dict1={"Mirror":"Ayana","Beautiful":"Khoobsurat","Toy":"Khilona"}

    print(f"Dictionary is:{dict1}")
    print(f"Keys of the dictionary:{dict1.keys()}")
    print(f"Values of the dictionary:{dict1.values()}")

    print("Enter the key to get its value:")
    key=input()

    val=dict1[key]
    print(f"The value of the {key} is {val}")

if __name__=="__main__":
    main()