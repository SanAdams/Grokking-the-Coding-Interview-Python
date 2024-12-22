def merge_intervals(intervals):
    output = []
    potential_merge = 1
    earliest_interval = intervals[0]

    if len(intervals) == 1:
        return intervals

    while potential_merge != len(intervals):

        # Non-overlapping intervals
        if earliest_interval[1] < intervals[potential_merge][0] and earliest_interval[1] < intervals[potential_merge][1]:
            output.append(earliest_interval)
            earliest_interval = intervals[potential_merge]

        # Overlapping intervals
        elif earliest_interval[0] <= intervals[potential_merge][0] and earliest_interval[1] <= intervals[potential_merge][1]:
            earliest_interval = [earliest_interval[0], intervals[potential_merge][1]]

        potential_merge += 1

    output.append(earliest_interval)
    return output

def main():
    all_intervals = [
        [[1, 5], [3, 7], [4, 6]],
        [[1, 5], [4, 6], [6, 8], [11, 15]],
        [[3, 7], [6, 8], [10, 12], [11, 15]],
        [[1, 5]],
        [[1, 9], [3, 8], [4, 4]],
        [[1, 2], [3, 4], [8, 8]],
        [[1, 5], [1, 3]],
        [[1, 5], [6, 9]],
        [[0, 0], [1, 18], [1, 3]]
    ]

    for i in range(len(all_intervals)):
        print(i + 1, ". Intervals to merge: ", all_intervals[i], sep="")
        result = merge_intervals(all_intervals[i])
        print(result)
        print("-"*100)


if __name__ == '__main__':
    main()