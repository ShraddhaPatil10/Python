def main():
    try:
        f=open("1.txt",'r')
        f=open("2.txt",'r')
        f=open("3.txt",'r')


    except Exception:
        print("Files not found!!!")

if __name__=="__main__":
    main()