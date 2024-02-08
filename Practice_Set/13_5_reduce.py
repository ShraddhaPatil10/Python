from functools import reduce

def main():
    numbers=[3,2,4,5,9,10]

    max_num=reduce(lambda x,y:x if x>y else y,numbers)

    print("Maximum number:",max_num)

if __name__=="__main__":
    main()