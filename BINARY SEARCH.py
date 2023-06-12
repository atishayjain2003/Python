n=int(input("Enter number of elements in array"))
L=[]
for i in range(n):
    x=int(input("Enter the element"))
    L.append(x)
#print(L)
result=-1
p=int(input("Enter the element to be searched"))
start=0
end=len(L)-1
while (start<=end):
    mid=(start+end)//2
    if p > L[mid]:
        start=mid+1
    elif p < L[mid]:
        end=mid-1
    elif p==L[mid]:
        result=mid
        break
if (result==-1):
    print("ELEMENT IS NOT PRESENT")
else:
    print("ELEMENT IS PRESENT")
        
