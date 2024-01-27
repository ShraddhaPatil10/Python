def main():
    print("Enter the post:")
    post=input()

    if "harry" in post.lower():
        print("Post is talking about harry")
    else:
        print("Post is not talking about harry")


if __name__=="__main__":
    main()