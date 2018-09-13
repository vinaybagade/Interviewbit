class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        start = 0
        globalstart = -1
        end = -1
        globalsum = -1
        globallength = 0
        currentsum = 0
        for i in range(0,len(A)):
            if A[i] >= 0:
                currentsum += A[i]
                if currentsum > globalsum or currentsum==globalsum and  i - start + 1 > globallength:
                    globalsum = currentsum
                    globalstart = start
                    end = i
                    globallength = i - start + 1
            else:
                start = i + 1
                currentsum = 0
        if end == -1:
            return []
        return A[globalstart:end+1]
                    
            
