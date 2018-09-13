class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if len(A) == 0:
            return -1
        input = [(A[i],i) for i in range(0,len(A))]
        input.sort(key = lambda x: x[0])
        subarray = [0]*len(A)
        maxj = input[-1][1]
        for i in range(len(input)-1,-1,-1):
            subarray[i] = maxj
            if input[i][1] > maxj:
                maxj = input[i][1]
            
        answer = -1
        
        for i in range(0,len(A)):
            answer = max(answer,subarray[i]-input[i][1])
        return answer
