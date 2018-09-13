class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if len(A) <= 1:
            return 0
        minimum = min(A)
        maximum = max(A)
        gap = (maximum-minimum)/float(len(A)) 
        bucket = [[maximum+1,minimum-1] for i in range(len(A)+1)]
        if gap == 0:
            return 0
        for i in range(0,len(A)):
            bucket_index = int((A[i] - minimum)/gap)
            print bucket_index
            bucket[bucket_index][0] = min(bucket[bucket_index][0],A[i])
            bucket[bucket_index][1] = max(bucket[bucket_index][1],A[i])
        max_diff = 0
        
        prev = bucket[0][1]
        for i in range(1,len(bucket)):
            if bucket[i][1] == minimum-1 and bucket[i][0] == maximum+1:
                continue
            max_diff = max(max_diff,bucket[i][0]-prev)
            prev = bucket[i][1]
        return max_diff
            
