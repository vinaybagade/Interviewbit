class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        maxsumsofar = max(A)
        currentsum = 0
        for i in range(0,len(A)):
            currentsum += A[i]
            if currentsum > maxsumsofar:
                maxsumsofar = currentsum
            if currentsum < 0:
                currentsum = 0
        return maxsumsofar
