class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        if A == 0:
            return [1]
        prevrow = [1,1]
        currentrow = [1,1]
        for j in range(1,A):
            currentrow = [prevrow[i]+prevrow[i+1] for i in range(0,len(prevrow)-1)]
            currentrow = [1] + currentrow + [1]
            prevrow = currentrow
        return currentrow
