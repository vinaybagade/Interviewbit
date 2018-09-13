class Solution:
    # @param A : string
    # @return a list of integers
    def flip(self, A):
        numones = 0
        numzeros = 0
        begin = 0
        end = 0
        maxnum = -1
        ansbegin = 0
        ansend = 0
        for i in range(0,len(A)):
            if A[i] == '0':
                numzeros +=1
            else:
                numones +=1
            if numzeros >= numones:
                if maxnum < (numzeros - numones):
                    maxnum = numzeros - numones
                    ansbegin = begin
                    ansend = i
            else:
                numzeros = 0
                numones = 0
                begin = i + 1
        
        if maxnum == -1:
            return []
        return [ansbegin+1,ansend+1]
