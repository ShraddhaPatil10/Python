def Add(No):
    if(No<=0):
        return 0

    else:
        return (No+Add(No-1))
        
ret=Add(4)
print("Addition is:",ret)