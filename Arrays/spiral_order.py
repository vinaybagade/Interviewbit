        

class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, A):
        matrix = [[0]*A for i in range(0,A)]
        direction = 1
        i = 0
        j = 0
        for val in range(1,A**2+1):
            matrix[i][j] = val
            if direction == 1:
                if j+1 >= A or matrix[i][j+1] != 0:
                    direction = 2
                    i +=1
                else:
                    j +=1
                continue
            elif direction == 2:
                if i+1 >= A or matrix[i+1][j]!= 0:
                    direction = 3
                    j = j -1
                else:
                    i +=1
                continue
            elif direction == 3:
                if j-1 <= -1 or matrix[i][j-1]!=0:
                    direction = 4
                    i = i - 1
                else:
                    j= j-1
            else:
                if i-1 <= 0 or matrix[i-1][j] !=0:
                    direction = 1
                    j = j+1
                else:
                    i = i-1
        return matrix
