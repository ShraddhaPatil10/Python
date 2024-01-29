def main():
    l1=["harry","sachine","soham","rahul"]

    for i in range(0,len(l1),1):
        if l1[i].startswith("s"):
            print(f"Good Morning {l1[i]}")

if __name__=="__main__":
    main()