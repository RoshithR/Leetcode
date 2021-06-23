# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

def mergeIntervals(intervals):
    intervals.sort(key=lambda x:x[0])
    merged_intervals=[]
    for interval in intervals:
        if not merged_intervals or merged_intervals[-1][1]<interval[0]:
            merged_intervals.append(interval)
        else:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
    return merged_intervals

intervals = [[1,3],[2,6],[8,10],[15,18]]
print(mergeIntervals(intervals))


