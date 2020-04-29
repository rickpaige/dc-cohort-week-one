num = int(input("Enter a number "))

if num >= 1:
    for i in range(2, num):
         if(num % i) == 1:
            print("The number is",num, "a prime number")
            break

    else:
        print("The number",num, "is not prime")