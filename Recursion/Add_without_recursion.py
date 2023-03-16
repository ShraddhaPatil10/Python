def Add(No):
    sum=0
    while(No>0):
        sum=sum+No
        No=No-1
    return sum

ret=Add(4)
print("Addition is:",ret)