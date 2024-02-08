def Multiply(l1):
    return l1%5==0

    return l

def filterx(Arr,helper_fun):
    res=[]
    for no in Arr:
        if(helper_fun(no)):
            res.append(no)

    return res

def main():
    l1=[10,34,15,55,35,8,3,90]

    filter_list=filterx(l1,Multiply)

    print("Data after filter is:",filter_list)


if __name__=="__main__":
    main()