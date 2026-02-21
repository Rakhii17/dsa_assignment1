# Naive Recursive Fibonacci Program

def fibonacci(n):
 # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
# Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Enter position: "))

if num < 0:
    print("Invalid input! Fibonacci is not defined for negative numbers.")
else:
    result = fibonacci(num)
    print("Fibonacci at position", num, "is:", result) 
    
    
    
    # Memoized Recursive Fibonacci Program

# Dictionary to store already calculated Fibonacci values
data = {}

def fibonacci(n):
    # Base case: if n is 0 or 1, return n
    if n <= 1:
        return n
    
    if n not in data:
        data[n] = fibonacci(n-1) + fibonacci(n-2)
    
    return data[n]

num = int(input("Enter position: "))

if num < 0:
    print("Invalid input! Fibonacci is not defined for negative numbers.")
else:
    print("Fibonacci:", fibonacci(num))