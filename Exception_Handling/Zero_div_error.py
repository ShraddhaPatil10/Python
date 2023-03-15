def main():
    try:
        print("Enter 1st number:")
        no1=int(input())

        print("Enter 2nd number:")
        no2=int(input())

        Ans=no1/no2
        print("Division is:",Ans)

    except ZeroDivisionError:
        print("Inside zero division error:")

    except ValueError:
        print("Inside value erroe")

    except Exception:
        print("Inside last except block")

    finally:
        print("Inside finally block")

if __name__=="__main__":
    main()