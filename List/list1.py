values=[10,20,30,40]
print("values are:",values)
print("Data type is:",type(values))
print("Length is:",len(values))

print("******************************************")
print(values[0])
print(values[1])
print(values[2])
print(values[3])

print("*********************************************")

values.append(50)
print("Data after append:",values)

print("******************************************")
values.remove(20)
print("Data after removal:",values)

print("********************************************")
values.insert(1,20)
print("Data after insertion:",values)

print("********************************************")
print(type(values[0]))