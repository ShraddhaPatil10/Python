def main():
    l1=[23,4,32,56,21]

    for index,item in enumerate(l1):
        if index==0:
            continue
        elif index==1:
            continue
        elif index==3:
            continue
        print(f"{index+1} element is:{item}")

if __name__=="__main__":
    main()