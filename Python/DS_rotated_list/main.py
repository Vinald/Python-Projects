def find_rotation_count(arr):
    left, right = 0, len(arr) - 1

    while left <= right:
        # If the array is already sorted (no rotation), the smallest element is at index 0
        if arr[left] <= arr[right]:
            return left

        mid = (left + right) // 2
        next_index = (mid + 1) % len(arr)
        prev_index = (mid - 1 + len(arr)) % len(arr)

        # Check if mid element is the minimum
        if arr[mid] <= arr[next_index] and arr[mid] <= arr[prev_index]:
            return mid

        # Decide which half to choose
        if arr[mid] >= arr[left]:
            left = mid + 1
        else:
            right = mid - 1

# Example usage
arr = [5, 6, 9, 0, 2, 3, 4]
rotation_count = find_rotation_count(arr)
print("The array was rotated", rotation_count, "times.")

# Test case 1: Standard rotation
arr1 = [5, 6, 9, 0, 2, 3, 4]
# Expected output: 3 (the array was rotated 3 times)
assert find_rotation_count(arr1) == 3

# Test case 2: No rotation (already sorted)
arr2 = [1, 2, 3, 4, 5, 6, 7]
# Expected output: 0 (the array was not rotated)
assert find_rotation_count(arr2) == 0

# Test case 3: Full rotation (back to original)
arr3 = [3, 4, 5, 6, 7, 1, 2]
# Expected output: 5 (rotated 5 times to bring smallest element to the front)
assert find_rotation_count(arr3) == 5

# Test case 4: Single element
arr4 = [10]
# Expected output: 0 (one element, so no rotation)
assert find_rotation_count(arr4) == 0

# Test case 5: Two elements, rotated once
arr5 = [20, 10]
# Expected output: 1 (rotated 1 time to get smallest element at the front)
assert find_rotation_count(arr5) == 1

# Test case 6: Minimal rotation (rotated once)
arr6 = [6, 7, 1, 2, 3, 4, 5]
# Expected output: 2 (rotated twice)
assert find_rotation_count(arr6) == 2

# Test case 7: Array with large rotation near its length
arr7 = [9, 12, 15, 18, 2, 5, 6]
# Expected output: 4 (rotated 4 times)
assert find_rotation_count(arr7) == 4

# Test case 8: Edge case - array rotated by half of its length
arr8 = [3, 4, 5, 1, 2]
# Expected output: 3 (rotated 3 times)
assert find_rotation_count(arr8) == 3

print("All test cases passed.")
