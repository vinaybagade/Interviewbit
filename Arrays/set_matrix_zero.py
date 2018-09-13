class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        if len(A) == 0:
            return A
        column = False
        row = False
        for i in range(0,len(A)):
            if len(A[i]) == 0:
                return A
            if A[i][0] == 0:
                column = True
                
                
        for j in range(0,len(A[0])):
            if A[0][j] == 0:
                row = True
        
        
        for i in range(1,len(A)):
            for j in range(1,len(A[i])):
                if A[i][j] == 0:
                    A[i][0] = -1
                    A[0][j] = -1
                    
        for i in range(1,len(A[0])):
            if A[0][i] == -1 or A[0][i] == 0:
                for j in range(1,len(A)):
                    A[j][i] = 0
        
        for i in range(1,len(A)):
            if A[i][0] == -1 or A[i][0] == 0:
                for j in range(1,len(A[i])):
                    A[i][j] = 0
                    
        for i in range(0,len(A)):
            
            if column or A[i][0] == -1:
                A[i][0] = 0
                
        for j in range(0,len(A[0])):
            
            if row or A[0][j] == -1:
                A[0][j] = 0
                
        return A
