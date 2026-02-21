🔁 Recursion Algorithms – Implementation & Complexity Study



📌 Project Introduction
Recursion works by breaking a problem into smaller subproblems of the same type until a base condition is reached. Each recursive call adds a new frame to the call stack, making it important to analyze both time and memory usage.

The objective of this project is to:
Explore different recursion patterns
Compare naive and optimized recursive approaches
Analyze time complexity using recurrence relations
Study recursion depth and stack behavior
Understand efficiency differences across algorithms

🧮 1️⃣ Factorial Using Recursion
Factorial represents a linear recursive problem where each call reduces the problem size by exactly one.

n!=n×(n−1)!
The recursion continues until it reaches the base case (0 or 1).

Characteristics
One recursive call per function
Linear reduction in input size
Straightforward stack growth
Complexity Analysis

Time Complexity:
O(n) — one multiplication per recursive level
Space Complexity:
O(n) — recursion depth equals n

🔢 2️⃣ Fibonacci Sequence (Recursive Approaches)
The Fibonacci sequence is defined as:
F(n)=F(n−1)+F(n−2)

Two approaches were implemented to study performance differences.

🔹 A. Naive Recursive Fibonacci
Each call generates two new recursive calls
Creates a binary recursion tree
Many intermediate values are recalculated

Why It Is Inefficient

 recalculates Fibonacci multiple times.
This repeated computation leads to exponential growth.

Complexity
Time Complexity: O(2ⁿ)
Space Complexity: O(n) (due to recursion stack)

🔹 B. Memoized Fibonacci 
In this version, previously computed values are stored in a dictionary and reused.

Advantages
Each Fibonacci number is computed only once
No repeated subproblems
Converts exponential behavior into linear

Complexity
Time Complexity: O(n)
Space Complexity: O(n)


🗼 3️⃣ Tower of Hanoi

Tower of Hanoi is a classic example of recursive problem decomposition.

Recursive Strategy
Move n-1 disks to helper rod
Move the largest disk to destination
Move n-1 disks from helper to destination


What It Demonstrates

Divide-and-conquer thinking
Recursive problem breakdown
Rapid growth in recursive calls
Recurrence Relation

T(n)=2T(n−1)+1
Complexity

Time Complexity: O(2ⁿ)
Space Complexity: O(n)

A full movement trace was analyzed for N = 3 to understand recursive execution order.

🔎 4️⃣ Recursive Binary Search

Binary search is a divide-and-conquer algorithm that works on sorted arrays.
Instead of checking every element, it repeatedly divides the search space into half.

Recurrence Relation
T(n)=T(n/2)+c

Where:
Problem size reduces by half
Constant work is done at each step
Solving the Recurrence
After repeated expansion:

T(n)=O(logn)


Complexity

Time Complexity: O(log n)
Space Complexity: O(log n)


📊 Complexity Comparison Summary
Algorithm	Time Complexity	Space Complexity	Type of Growth
Factorial	O(n)	O(n)	Linear
Fibonacci (Naive)	O(2ⁿ)	O(n)	Exponential
Fibonacci (Memoized)	O(n)	O(n)	Linear
Tower of Hanoi	O(2ⁿ)	O(n)	Exponential
Binary Search	O(log n)	O(log n)	Logarithmic


🏁 Final Conclusion

Recursion provides elegant and readable solutions, but efficiency depends on:
Number of recursive calls
Presence of overlapping subproblems
Depth of recursion
Use of optimization techniques

By comparing naive and optimized approaches, this project highlights the importance of analyzing recursion
