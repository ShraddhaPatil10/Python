def main():
    print("Enter your username:")
    username=input()

    if len(username)<10:
        print("Less than 10 characters in the username")
    else:
        print("More than 10 characters in username")

if __name__=="__main__":
    main()