print("***************Using While***************")
def Display(No):
    while(No>0):
        print(No)
        No=No-1

Display(4)

print("\n\n***************Using Recursion***************")
def display(No):
    if(No>0):               ##Replace while by if
        print(No)
        No=No-1
        display(No)

display(4)