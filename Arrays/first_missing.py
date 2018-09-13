class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        j = 0
        for i in range(0,len(A)):
            if A[i] > 0:
                A[i],A[j] = A[j],A[i]
                j +=1
                
        for i in range(0,j):
            if abs(A[i])-1 < j and A[abs(A[i])-1] > 0:
                A[abs(A[i])-1] = - A[abs(A[i])-1]
        missing = j + 1
        for i in range(0,j):
            if A[i] > 0:
                missing = i+1
                break
        return missing    
        
