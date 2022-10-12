print("Demonstration of list")

#Characteristics of list
#data:Hetrogeneous
#ordered:Yes
#Indexed:Yes
#Mutable:Yes    (Mutable means changable--->Mutablity based on whole data
#Duplicates:Yes

data=[11,21,51,101,21,11]       #Allows Duplicates
data1=[10,12.5,True,"Hello"]    #Hetrogeneous

print("Data is hetrogeneous:",data1)
print("Data is ordered:",data1)
print("Data at index 2 is:",data1[2])
print("Data allows duplicates:",data)

print("List is mutable")
data1.append(201)
print("Data after append:",data1)

data.pop()
print("Data after pop:",data1)

