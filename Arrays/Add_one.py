class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        index = 0
        for i in range(0,len(A)):
            if A[i] != 0:
                index = i
                break
        answer = []
        carry = 1
        for i in range(len(A)-1,index-1,-1):
            if carry + A[i] > 9:
                answer.append(0)
                carry = 1
            else:
                answer.append(A[i]+carry)
                carry = 0
        if carry == 1:
            answer.append(1)
        return reversed(answer)
