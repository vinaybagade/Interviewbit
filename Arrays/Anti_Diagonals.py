class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        answer = []
        for i in range(0,len(A)):
            diag = [A[j][i-j] for j in range(0,i+1)]
            answer.append(diag)
        for i in range(1,len(A)):
            diag = [A[i+j][len(A)-1-j] for j in range(0,len(A)-i)]
            answer.append(diag)
        return answer
