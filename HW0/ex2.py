def ispalindrome(arr):

    # Base case 1: empty array
    # An empty array has no elements, so it reads the same forwards and backwards, making it a palindrome by definition.
    if len(arr) == 0:
        return True

    # Base case 2: single element
    # A single element array reads the same forwards and backwards, so it is also a palindrome.
    if len(arr) == 1:
        return True

    # Check first and last elements
    # If the first and last elements of the array are not the same, then the array cannot be a palindrome, so we return False.
    if arr[0] != arr[-1]:
        return False

    # Recursive call
    # At this point, the first and last elements are deemed to be the same, so we can ignore them and check the remaining subarray (which is the original array without the first and last elements) for being a palindrome. This is done by making a recursive call to the function with the subarray arr[1:-1].
    return ispalindrome(arr[1:-1])

print(ispalindrome([1,2,3,2,1]))  # True
print(ispalindrome([1,2,3,4,3]))  # False