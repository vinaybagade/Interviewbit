class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        intervals.sort(key = lambda x: x.start)
        answer = [intervals[0]]
        for i in range(1,len(intervals)):
            if answer[-1].end >= intervals[i].start:
                answer[-1].end = max(answer[-1].end,intervals[i].end)
            else:
                answer.append(intervals[i])
        return answer
