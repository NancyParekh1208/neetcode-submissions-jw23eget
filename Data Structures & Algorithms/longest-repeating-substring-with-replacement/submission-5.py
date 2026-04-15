class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 0 # longest valid window
        for i in range(len(s)):
            maxf = 0
            freq = {}
            for j in range(i, len(s)):
                freq[s[j]] = freq.get(s[j],0) + 1
                maxf = max(maxf, freq[s[j]])
                if (j-i+1) - maxf <= k:
                    res = max(res,j-i+1)
        
        return res

        