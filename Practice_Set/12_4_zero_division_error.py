def main():
    try:
        print("Enter 1st number:")
        no1=int(input())

        print("Enter 2nd number:")
        no2=int(input())

        res=int(no1/no2)

        print(f"{no1}/{no2}={res}")

    except ZeroDivisionError:
        print("Zero division error")
    except Exception:
        print("Error")

if __name__=="__main__":
    main()