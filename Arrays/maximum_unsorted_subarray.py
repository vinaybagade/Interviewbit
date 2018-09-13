class Solution:
    # @param A : list of integers
    # @return a list of integers
    def subUnsort(self, A):
        A_min = [0]*len(A)
        A_max = [0]*len(A)
        maximum = -1
        minimum = max(A)
        for i in range(0,len(A)):
            if maximum < A[i]:
                maximum = A[i]
            A_max[i] = maximum
        for i in range(len(A)-1,-1,-1):
            if A[i] < minimum:
                minimum = A[i]
            A_min[i] = minimum
        
        start = -1
        end = -1
        
        for i in range(0,len(A)):
            if A_min[i]!=A_max[i]:
                start = i
                break
        for i in range(len(A)-1,-1,-1):
            if A_min[i] != A_max[i]:
                end = i
                break
        if start == -1 and end == -1:
            return [-1]
        return [start,end]
                
