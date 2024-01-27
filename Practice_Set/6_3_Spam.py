def main():
    sentence=input("Enter the sentence:")
    l1=["make a lot of money","buy now","subscribe this","click this"]

    cnt=0
    for i in range(len(l1)):
        if l1[i] in sentence.lower():
            cnt=cnt+1
    if cnt>=1:
        print("Given sentence is spam")
    else:
        print("Given sentence is not spam")

if __name__=="__main__":
    main()