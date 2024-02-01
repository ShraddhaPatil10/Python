import os
def main():
    oldname="Sample.txt"
    newname="renamed_by_python.txt"

    with open(oldname) as f:
        content=f.read()

    with open(newname,'w') as f:
        f.write(content)

    os.remove(oldname)

if __name__=="__main__":
    main()