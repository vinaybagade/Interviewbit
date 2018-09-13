class Solution:
    # @param A : list of integers
    # @return the same list of integer after modification
    def nextPermutation(self, A):
        if len(A) < 2:
            return A
        pivot = -1
        for i in range(len(A)-1,0,-1):
            if A[i-1] < A[i]:
                pivot = i-1
                break
        if pivot == -1:
            A.sort()
            return A
        MIN = max(A) + 1
        MIN_INDEX = -1
        for i in range(pivot+1,len(A)):
            if A[i] > A[pivot] and A[i] < MIN:
                MIN = A[i]
                MIN_INDEX = i
        A[pivot],A[MIN_INDEX] = A[MIN_INDEX],A[pivot]
        A[pivot+1:]=sorted(A[pivot+1:])
        return A
        
