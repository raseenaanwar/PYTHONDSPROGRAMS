def two_sum(nums, target):
    # Create a dictionary to store the indices of elements
    num_indices = {}

    # Iterate through the list of numbers
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num

        # Check if the complement is already in the dictionary
        if complement in num_indices:
            # Return the indices of the two numbers that add up to the target
            return [num_indices[complement], i],num_indices

        # If the complement is not in the dictionary, add the current number and its index
        num_indices[num] = i

    # If no solution is found
    return None

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result,r = two_sum(nums, target)
print(result)
print(r)
