'''
Number Pattern
Send Feedback
Print the following pattern for n number of rows.
Note: each line consist of equal number of characters + spaces. Suppose you are printing xth line for N=n. You need to print 1..x followed by (n-x) spaces, again (n-x) spaces followed by x..1
For eg. N = 5 

Sample Input 1 :
4
Sample Output 1 :





1              1
12          21
123      321
1234   4321
1234554321













'''n=int(input("Enter number of rows"))
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
