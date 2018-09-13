class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        numsteps = 0
        for i in range(0,len(A)-1):
            numsteps += max(abs(A[i+1]-A[i]),abs(B[i+1]-B[i]))
        return numsteps
