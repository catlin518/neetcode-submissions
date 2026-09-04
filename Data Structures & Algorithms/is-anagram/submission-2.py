class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)

        #方法2
        if len(s) != len(t):
            return False
        
        record = [0] * 26
        for char in s:
            record[ord(char) - ord('a')] += 1
        for char in t:
            record[ord(char) - ord('a')] -= 1
        
        for count in record:
            if count != 0:
                return False
        return True

