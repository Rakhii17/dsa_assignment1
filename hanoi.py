
# Tower of Hanoi using Recursion

def hanoi(n, source, helper, destination):
    # Base Case:
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return  
    
    # Move n-1 disks from source to helper
    hanoi(n-1, source, destination, helper)
  
    # Move the nth (largest) disk from source to destination
    print("Move disk", n, "from", source, "to", destination)
    
    # Move the n-1 disks from helper to destination
    hanoi(n-1, helper, source, destination)

num = int(input("Enter number of disks: "))
if num <= 0:
    print("Invalid input! Number of disks must be a positive integer.")
hanoi(num, 'A', 'B', 'C')


# Time Complexity = O(2^n) 
# Space Complexity = O(n)