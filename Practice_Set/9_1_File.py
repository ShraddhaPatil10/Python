def main():
    f=open("Poem.txt","r")
    content=f.read()
    print("Content from file is:\n",content)

    if "twinkle" in content :
        print("Twinkle is present")
    else:
        print("Twinkle is not present")

    f.close()

if __name__=="__main__":
    main()