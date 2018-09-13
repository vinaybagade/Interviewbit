def cmp(A,B):
    if str(A)+str(B) > str(B)+str(A):
        return -1
    elif str(A)+str(B) > str(B)+str(A):
        return 1
    return 0
class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = list(A)
        A.sort(cmp)
        answer = ""
        for num in A:
            answer = answer + str(num)
        answer = answer.lstrip("0")
        if len(answer):
            return answer
        return "0"
            
