#Lists are Mutable data types
#Mutability means values in lists can be changed
#list sequencing
n=int(input("Enter number of elements in list"))
L=[]
print("Enter list elements")
for i in range(n):
    x=int(input())
    L.append(x)
#L[start:end:step]
#the loop runs till end -1
y=L[1::]
print(y)
#The above statement means that starting from index 1 all the elements will be displayed