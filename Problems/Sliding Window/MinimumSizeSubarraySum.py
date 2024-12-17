# The problem: https://leetcode.com/problems/minimum-size-subarray-sum/
def minimum_size_subarray_optimal(target, nums):
    # We want to initialize a window
    # The window expands with the end variable
    # We want it to expand until the current sum either reaches or exceeds the target
        # The window shrinks when we increment the start variable
        # subtracting numbers that are falling outside the window
        # calculate the current length and compare to the minimum
    # Return the minimum length
    # [1,2,2,1] target: 2
    # 


    start = 0
    min_length = float('inf')
    current_sum = 0
    for end in range(len(nums)):
        current_sum += nums[end]

        while current_sum >= target:
            min_length = min(end - start + 1, min_length)
            current_sum -= nums[start]
            start += 1
    
    return min_length if min_length != float('inf') else 0


def minimum_size_subarray_sum_naive(target: int, nums: list[int]) -> int:
    start = 0
    min_length = float('inf')

    for end in range(len(nums)):
        subarray = nums[start:end + 1]
        subarray_sum = 0
        for i in range(len(subarray)):
            subarray_sum += subarray[i]
        
        if subarray_sum == target:
            min_length = min(subarray_sum, min_length)

    return min_length if min_length != float('inf') else 0

