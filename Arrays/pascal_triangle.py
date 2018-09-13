class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        if A == 0:
            return []
        pascal = [[1]]
        for i in range(1,A):
            current_row = [pascal[-1][i] + pascal[-1][i+1] for i in range(0,len(pascal[-1])-1) ]
            current_row = [1] + current_row + [1]
            pascal.append(current_row)
        return pascal
