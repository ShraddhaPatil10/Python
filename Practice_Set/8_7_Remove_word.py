import os
def main():
    l1=["Shraddha","Onkar","Vivek","Sam","Avani"]
    print(f"Original list is:{l1}")
    print("Enter the word to remove from list:")
    word=input()

    l1.remove(word)
    print(f"After removing element list is {l1}")

if __name__=="__main__":
    main()