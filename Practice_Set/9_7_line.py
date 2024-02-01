def main():
    content=True
    i=1
    with open("log_file.txt") as f:
        while content:
            i += 1
            content=f.readline()

            if 'python' in content.lower():
                print("yes python is present")
                print(content)
                print(i)

if __name__=="__main__":
    main()