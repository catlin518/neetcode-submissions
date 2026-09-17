class Solution:
    def isPalindrome(self, s: str) -> bool:
        #1.isalnum()
        newStr = ""
        
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]