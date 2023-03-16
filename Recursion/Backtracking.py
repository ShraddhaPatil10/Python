#Print 0 to 3
def Display(No):        ##Backtracking
    if(No>0):
        No=No-1
        Display(No)
        print(No)

Display(4)