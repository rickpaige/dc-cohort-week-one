n = input("Enter a number: ")
fact = 1
if int(n) >= 1:
    for i in range (1,int(n)+1):
        fact = fact * i
print("The factorial of ",n , " is : ",fact)

