# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        temp = Interval(min(new_interval.start,new_interval.end),max(new_interval.start,new_interval.end))
        
        for i in range(0,len(intervals)):
            if intervals[i].start > temp.start:
                intervals.insert(i,temp)
                break
            else:
                if i == len(intervals)-1:
                    intervals.append(temp)
        if len(intervals) == 0:
            intervals.append(temp)
        answer = [intervals[0]]
        for i in range(1,len(intervals)):
            if answer[-1].end > intervals[i].start:
                answer[-1].end = max(answer[-1].end,intervals[i].end)
            else:
                answer.append(intervals[i])
        return answer
                    
