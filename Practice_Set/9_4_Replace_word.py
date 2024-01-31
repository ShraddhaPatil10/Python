def main():
    text="donkey"
    replace="######"
    with open(r"Donkey_Replace.txt","r") as file:
        f=file.read()
        f=f.replace(text,replace)

    with open(r"Donkey_replace.txt","w") as file:
        file.write(f)

    print("done")

if __name__=="__main__":
    main()