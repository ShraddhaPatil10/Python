import random
def main():
    print("************************************WELCOME************************************")
    print("-------------------Snake Water Gun Game-------------------")

    print("Enter your choice:\n1 for Snake\n2 for Water\n3 for Gun")

    Comp=random.randint(1,3)

    You=int(input("Enter:"))

    if Comp==You:
        print("Oooops Tie!!!")

    else:
        if Comp==1:
            if You==2:
                print("Computer Win!!!")
            elif You==3:
                print("You Win!!!")

        if Comp==2:
            if You==1:
                print("You Win!!!")
            elif You==3:
                print("Computer Win!!!")

        if Comp==3:
            if You==1:
                print("Computer Win!!!")
            elif You==2:
                print("You Win!!!")

    print(f"Computer choice is {Comp} and your choice is {You}")
                
if __name__=="__main__":
    main()