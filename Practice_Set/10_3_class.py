class Demo:
    a=10
    #print("Value of a:",Demo.a)

def main():
    obj=Demo()
    print("Value of a:", Demo.a)
    obj.a=0
    print("Value of a:", Demo.a)
    Demo.a=0
    print("Value of a:", Demo.a)



if __name__=="__main__":
    main()