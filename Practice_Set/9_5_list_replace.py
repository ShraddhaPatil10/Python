def main():
    words=["donkey","mote","hello"]

    with open("Donkey_Replace.txt") as f:
        content=f.read()

    for word in words:
        content=content.replace(word,"$#%@*")

        with open("Donkey_Replace.txt",'w') as f:
            f.write(content)

if __name__=="__main__":
    main()