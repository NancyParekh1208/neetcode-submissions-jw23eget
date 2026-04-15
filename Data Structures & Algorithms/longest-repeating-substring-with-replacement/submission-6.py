class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        charSet = set()
        for ch in s:
            charSet.add(ch)
        res = 0
        for c in charSet:
            l = 0 
            count = 0
            for r in range(len(s)):
                if s[r] == c:
                    count+=1 # same char count

                while (r-l+1) - count > k: # need more than k replacements to make every char c
                    if s[l] == c:
                        count -= 1
                    l+=1
                res = max(res, r-l+1)
        
        return res