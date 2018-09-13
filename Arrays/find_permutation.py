class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        if A == "":
            return []
        start = 2
        for i in A[:-1]:
            if i == 'I':
                start +=1
        ans = [ 0 for i in range(0,B)]
        MAX = start + 1
        ans_index = B-1
        for i in range(len(A)-1,-1,-1):
            if i == len(A) -1:
                if A[i] == 'I':
                    ans[-1] = start
                    ans[-2] = start -1
                else:
                    ans[-1] = start -1
                    ans[-2] = start
                start = start - 2
                ans_index = ans_index -2
            else:
                if A[i] == 'I':
                    ans[ans_index] = start
                    start -=1
                else:
                    ans[ans_index] = MAX
                    MAX +=1
                ans_index -=1
        return ans
                
