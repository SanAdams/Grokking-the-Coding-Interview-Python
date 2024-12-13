"""

 I'd like to find out if the window is just one element when we are appending to the output list

"""

def clean_up(i, current_window, nums):
    # remove all the indexes from current_window whose corresponding values are smaller than or equal to the current element
    while current_window and nums[i] >= nums[current_window[-1]]:
        print(f"\t\tAs nums[{i}] = {nums[i]} is greater than or equal to nums[{current_window[-1]}] = {nums[current_window[-1]]},")
        print(f"\t\tremove {current_window[-1]} from current_window")
        del current_window[-1]

def find_max_sliding_window(nums, w):
    # If the length of input list is 1, return the input list
    if len(nums) == 1:
        return nums
    
    # initializing variables
    output = []
    current_window = []

    print("\n\tFinding the maximum in the first window:")
    
    # iterate over the first w elements
    for i in range(w):
        print(f"\tAdding nums[{i}] = {nums[i]} to the first window:\n\t\tInitial state of current_window: {current_window}")
        # for every element, remove the previous smaller elements from current_window
        clean_up(i, current_window, nums)

        # append the index of the current element to current_window
        current_window.append(i)
        print(f"\t\tFinal state of current_window: {current_window}")

    # appending the maximum element of the current window to the output list
    output.append(nums[current_window[0]])

    print("\n\tFinding the maximum in the remaining windows:")

    # iterate over the remaining input list
    for i in range(w, len(nums)):
        print(f"\tAdding nums[{i}] = {nums[i]} to current_window:\n\t\tInitial state of current_window: {current_window}")

        # for every element, remove the previous smaller elements from current_window
        clean_up(i, current_window, nums)

        # remove first index from the current_window if it has fallen out of the current window
        if current_window and current_window[0] <= (i - w):
            print(f"\t\tIndex {current_window[0]} has fallen out of the current window,")
            print(f"\t\tso, remove it")
            del current_window[0]

        # append the index of the current element to current_window
        print(f"\t\tAppending {i} to current_window")
        current_window.append(i)
        print(f"\t\tFinal state of current_window: {current_window}")

        # appending the maximum element of the current window to the output list
        print(f"\tAppending the number at index {current_window[0]} = {nums[current_window[0]]}")
        output.append(nums[current_window[0]])

    # return the array containing output
    return output

find_max_sliding_window([1, 5, 8, 10, 10, 10, 12, 14, 15, 19, 19, 19, 17, 14, 13, 12, 12, 12, 14, 18, 22, 26, 26, 26, 28, 29, 30], 3)