def main():
    letter='''Dear <|Name|>
You are selected!
<|Date|>'''

    print("Enter your name:")
    name=input()

    print("Enter date:")
    date=input()

    letter=letter.replace("<|Name|>",name)
    letter=letter.replace("<|Date|>",date)

    print(letter)

if __name__=="__main__":
    main()