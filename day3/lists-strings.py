# List
['john', 'jane','sue']

greeting = "Hello"
print(greeting[0]) # Prints H
print(greeting[0::2]) # Prints Hlo

# Converting
print(greeting.lower()) 
print(greeting.upper()) 

# print(input("What is your name? ").lower())

# Split and Join
hello = "Hello, my name is Josh".split(" ") # prints ['Hello', 'my', 'name', 'is', 'Josh']
hello.pop() # removes last index Josh 
hello.append("Ricky")
hello  = " ".join(hello)
print(hello)

