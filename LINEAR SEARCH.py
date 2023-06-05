n=int(input("Enter the number:"))
l=[]
for i in range(n):
    a=int(input("Enter the numbers:"))
    l.append(a)
print("The list is:",l)    
max=l[0]       
for i in range(n):
    if(l[i]>max):
        max=l[i]
print("the maximum vale is", max)
                 
    
    
 
