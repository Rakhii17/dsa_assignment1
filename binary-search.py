def binary_search(arr, low, high, target):
    # Base case: element not found
    if low > high:
        return -1

    # Find middle index
    mid = (low + high) // 2

    # If element is found
    if arr[mid] == target:
        return mid

    # If target is smaller, search left half
    elif target < arr[mid]:
        return binary_search(arr, low, mid - 1, target)

    # If target is larger, search right half
    else:
        return binary_search(arr, mid + 1, high, target)
    
    
    
    """
Recursive Binary Search
Recurrence-Based Time Complexity Explanation

Let the size of the input array be n.
In recursive binary search:

1. We calculate the middle index.
2. We compare the target with the middle element.
3. We recursively search only ONE half of the array.

So at each step:
- Problem size reduces from n to n/2
- Extra work done per call is constant (O(1))

Step 1: Form the Recurrence Relation

T(n) = T(n/2) + c
Where:
T(n/2) -> recursive call on half of the array
c      -> constant work (mid calculation + comparison)


Step 2: Expand the Recurrence

T(n) = T(n/2) + c
     = T(n/4) + c + c
     = T(n/8) + 3c
     = T(n/2^k) + kc

Step 3: Find when recursion stops

Recursion stops when:
n / 2^k = 1
n = 2^k
k = log₂(n)

Step 4: Substitute back

T(n) = T(1) + c log n
Since T(1) is constant,
Final Time Complexity:
T(n) = O(log n)
Because recursive calls are made,
maximum recursion depth = log n

Space Complexity = O(log n)
"""