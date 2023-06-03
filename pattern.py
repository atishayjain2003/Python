n=int(input("Enter number of rows"))
for i in range(n):
    for j in range(1,i+2):
        print(j, end="")

    
    for j in range(i,n-1):
        print(" ", end="")

    for j in range(i,n-1):
        print(" ", end="")

    
    for j in range(i+1,0,-1):
        print(j, end="")
    print()
    
'''
Print The following pattern
1        1
12      21
123    321
1234  4321
1234554321
'''
