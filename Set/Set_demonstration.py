print("Demonstration of set")

MarvellousSet={11,"PPA",21,3.14,"Python"}

print(MarvellousSet)
print(len(MarvellousSet))

print("*****************************************")

MarvellousSet.remove(21)
print("Data after removal:",MarvellousSet)

MarvellousSet.discard(11)
print("Data after discarding:",MarvellousSet)

MarvellousSet.add("Angular")
print("Data after adding:",MarvellousSet)

print("*****************************************")