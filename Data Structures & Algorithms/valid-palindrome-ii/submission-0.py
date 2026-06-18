class Solution:
    def checkPalin(self, s:str) -> bool:
        left = 0
        right = len(s) - 1
        while left<=right:
            if s[left] != s[right]:
                return False
            
            left+=1
            right-=1
        
        return True
    def validPalindrome(self, s: str) -> bool:
        
        if self.checkPalin(s):
            return True
        
        for i in range(len(s)-1):
            newStr = s[:i] + s[i+1:]
            if self.checkPalin(newStr):
                return True
            

        return False

        