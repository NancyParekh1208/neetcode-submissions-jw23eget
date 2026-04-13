from collections import Counter
class Solution:

    def checkPermutation(self, s1: str, s2: str) -> bool:
        
        freq1 = Counter(s1)
        freq = Counter(s2)
        for key in freq1.keys():
            if key not in freq:
                return False
            elif freq[key] != freq1[key]:
                return False
        return True


    def checkInclusion(self, s1: str, s2: str) -> bool:
        # k = 3 and total_length = 7 ; check from 0 to 
        k = len(s1)
        flag = False
        for i in range(len(s2)-k+1):
            substr = s2[i:i+k]
            print(substr)
            flag = flag or self.checkPermutation(substr,s1)

        return flag
