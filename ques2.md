1️⃣ Factorial (Simple Recursion)

Time Complexity: O(n)
One recursive call for each value from n to 1
Total calls = n
Each call performs one multiplication
Linear growth

➡ Time Complexity = O(n)
➡Space Complexity: O(n)

Maximum recursion depth = n
Stack space grows linearly
➡ Space Complexity = O(n)



2️⃣ Factorial (Memoized)

Time Complexity: O(n)

Each value from 0 to n computed once
No repeated subproblems
Linear number of computations

➡ Time Complexity = O(n)
➡Space Complexity: O(n)

Recursion stack depth = n
Storage structure size = up to n

➡ Space Complexity = O(n)



 3️⃣ Fibonacci (Simple Recursion)

Time Complexity: O(2^n)

Each call makes two recursive calls
fib(n) = fib(n-1) + fib(n-2)
Creates a binary recursion tree
Many values are recomputed multiple times
Exponential growth in number of calls

➡ Time Complexity = O(2^n)
➡Space Complexity: O(n)

Maximum recursion depth = n
➡ Space Complexity = O(n)



4️⃣ Fibonacci (Memoized)

Time Complexity: O(n)

Each Fibonacci value calculated only once
Stored values reused directly
No repeated calculations

➡ Time Complexity = O(n)
➡Space Complexity: O(n)

Recursion stack depth = n
Storage size = up to n

➡ Space Complexity = O(n)