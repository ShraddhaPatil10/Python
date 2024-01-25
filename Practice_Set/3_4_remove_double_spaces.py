def main():
    str="Hello  Guys,This is  Shraddha!!!"

    print(f"Original string is:{str}")
    str=str.replace("  "," ")
    print(f"String after removing white spaces:")
    print(str)

if __name__=="__main__":
    main()