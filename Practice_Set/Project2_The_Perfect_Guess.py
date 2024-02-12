import random

def main():
    no=random.randint(1,100)

    while True:
        print("Enter the number:")
        user=int(input())

        if user==no:
            print("Your guess is correct!!!")
            exit()
        elif no<user:
            print("Lower number please")
        elif no>user:
            print("Greater number please")

if __name__=="__main__":
    main()