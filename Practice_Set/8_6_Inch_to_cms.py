def Converter():
    print("Enter value in inch:")
    val=int(input())

    cms=val*2.54
    print(f"Value in cms is {cms}")

if __name__=="__main__":
    Converter()