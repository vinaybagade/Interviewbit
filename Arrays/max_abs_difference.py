class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        A_sub = [A[i]+i for i in range(0,len(A))]
        A_add = [A[i]-i for i in range(0,len(A))]
        return max((max(A_sub)-min(A_sub)),(max(A_add)-min(A_add)))
        
