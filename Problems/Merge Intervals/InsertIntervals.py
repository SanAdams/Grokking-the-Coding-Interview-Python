# We have a list of sorted-non overlapping intervals
# They are sorted
# First idea is to scan the entire list of existing intervals
# When we find an existing interval that ends before the existing we look to
# interval that comes after and determine if it starts before the new interval ends

# We can scan linearly, but if you have a sorted input you can find the elements you want faster with
# binary search

# WEE WOO WEE WOO we need to merge intervals as necesary
def insert_interval(existing_intervals, new_interval):
    output = []
    output.append(existing_intervals[0])

    for i in range (len(existing_intervals)):
        if existing_intervals[i][1] >= new_interval[0]:
            output.append([existing_intervals[i][0], new_interval[1]])
        
    return output

def main():
    new_interval = [[5, 7], [8, 9], [10, 12], [1, 3], [1, 10]]
    existing_intervals = [
        [[1, 2], [3, 5], [6, 8]],
        [[1, 3], [5, 7], [10, 12]],
        [[8, 10], [12, 15]],
        [[5, 7], [8, 9]],
        [[3, 5]]
    ]
    
    for i in range(len(new_interval)):
        print("Exiting intervals: ", existing_intervals[i], sep="")
        print("New interval: ", new_interval[i], sep="")
        output = insert_interval(existing_intervals[i], new_interval[i])
        print(output)
        print("-"*100)


if __name__ == "__main__":
    main()