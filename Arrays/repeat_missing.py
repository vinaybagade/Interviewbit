class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n=len(A)
        x=sum(range(1,n+1))-sum(A)
        y=sum([i**2 for i in range(1,n+1)])-sum([i**2 for i in A])
        b=((x**2) + y)//(2*x)
        a=(y-(x**2))//(2*x)
        return a,b
        
