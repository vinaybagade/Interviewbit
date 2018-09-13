import heapq
class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        arrive.sort()
        depart.sort()
        i = 0 
        j = 0
        numstations = 0
        maxnum = 0
        while i< len(arrive) and j < len(depart): 
            if arrive[i] < depart[j]:
                numstations +=1
                i +=1
            else:
                numstations -=1
                j +=1
            if numstations > maxnum:
                maxnum = numstations
        if maxnum <= K:
            return 1
        return 0
            
