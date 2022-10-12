print("Demonstration of list")

batches=["PPA","LB","Python","Angular"]

print(batches)
print(batches[0])
print(batches[1])
print(batches[1:])
print(batches[:3])
print(batches[-1])

print("***************************************")

print("We can store hetrogeneous data")
data1=[21,"Hello",43.45,True]
print(data1)

data2=[32,"Shraddha",54.43,False]

combined=(data1,data2)
print(combined)

print("*****************************************")

#Multiple methods to manipulate the list

batches.append("MEAN")
print("Data after append:",batches)

batches.insert(2,"LSP")
print("Data after insertion:",batches)

batches.pop()
print("Data after pop:",batches)

del batches[1:]
print("Data after delete operation:",batches)

batches.extend(["LB","Python","Angular","MEAN"])
print("Data after extend:",batches)

batches.sort()
print("Data after sort:",batches)

print("*******************************************************")