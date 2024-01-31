def main():
    with open("log_file.txt") as f:
        content=f.read()

    if 'python' in content.lower():
        print("yes")


if __name__=="__main__":
    main()