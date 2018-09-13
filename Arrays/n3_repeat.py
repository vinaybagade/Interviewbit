class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        candidates = {}
        for elem in A:
            if len(candidates) < 2:
                candidates[elem] = candidates[elem] +1 if elem in candidates else 1
                continue
            if elem not in candidates:
                for key in candidates.keys():
                    candidates[key] -= 1
                keys = candidates.keys()
                for key in keys:
                    if candidates[key] == 0:
                        candidates.pop(key)
            else:
                candidates[elem] += 1
        for key in candidates.keys():
            count = 0
            for elem in A:
                if elem == key:
                    count +=1
            if count > len(A)/3:
                return key
            
        return -1            
