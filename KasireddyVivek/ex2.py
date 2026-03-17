def ispalindrome(arr):

    # Base case 1: empty array
    if len(arr) == 0:
        return True

    # Base case 2: single element
    if len(arr) == 1:
        return True

    # Check first and last elements
    if arr[0] != arr[-1]:
        return False

    # Recursive call
    return ispalindrome(arr[1:-1])

print(ispalindrome([1,2,3,2,1]))  # True
print(ispalindrome([1,2,3,4,3]))  # False