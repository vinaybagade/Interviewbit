class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A) - 1
        for i in range(0,len(A)/2+1):
            for j in range(i,len(A)-i-1):
                temp = A[i][j]
                A[i][j] = A[n-j][i]
                A[n-j][i] = A[n-i][n-j] 
                A[n-i][n-j] = A[j][n-i]
                A[j][n-i] = temp
        return A
