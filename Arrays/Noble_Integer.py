class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        for index,value in enumerate(A):
            if (index==len(A)-1 and value == 0) or (index<len(A)-1 and value < A[index+1] and len(A)-1-index == value):
                return 1
        return -1
