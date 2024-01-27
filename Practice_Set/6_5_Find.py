def main():
    l1=["shraddha","vivek","onkar","shanaya","sam"]

    print("Enter the name:")
    name=input()

    if name.lower() in l1:
        print(f"{name} is present")
    else:
        print(f"{name} is not present")
        
if __name__=="__main__":
    main()