class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []

        # Sort intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        
        merged_intervals = [intervals[0]]
        
        for interval in intervals[1:]:
            # If the start of the current interval is less than or equal to the end of the last merged interval, merge them
            if interval[0] <= merged_intervals[-1][1]:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])
            else:
                merged_intervals.append(interval)
        
        return merged_intervals
