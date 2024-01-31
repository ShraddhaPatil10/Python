def game():
    return 65

def main():
    Score=game()

    with open("Hiscore.txt") as f:
        Hiscore=int(f.read())

    if Hiscore<Score:
        with open("Hiscore.txt","w") as f:
            f.write(str(Score))
            


if __name__=="__main__":
    main()