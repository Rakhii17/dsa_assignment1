# Naive Recursive Factorial
# This method does NOT store previously calculated values

def factorial(n):
    # Base case: 0! = 1 and 1! = 1
    if n <= 1:
        return 1
    
    # Recursive case: n! = n × (n-1)!
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
if num < 0:
    print("Invalid input! Factorial is not defined for negative numbers.")
else:
    print("Factorial:", factorial(num))
    
    
 # Memoized Recursive Factorial
# (This method stores already calculated values to avoid recalculation)

data = {}   # Dictionary to store factorial values
def factorial(n):
    # Base case: 0! = 1 and 1! = 1
    if n <= 1:
        return 1
    
    if n not in data:
        data[n] = n * factorial(n - 1)
    
    return data[n]

num = int(input("Enter a number: "))
if num < 0:
    print("Invalid input! Factorial is not defined for negative numbers.")
else:
    print("Factorial:", factorial(num))