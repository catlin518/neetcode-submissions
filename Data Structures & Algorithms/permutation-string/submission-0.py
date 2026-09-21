class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #1.确认长度
        if len(s1) > len(s2): return False
        #2.初始化
        s1Count, s2Count = [0]*26, [0]*26
        #3.先把len(s1)的部分录入
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        #4.先比对这几个match
        match = 0
        for i in range(26):
            match += (1 if s1Count[i] == s2Count[i] else 0)

        #5.开始比对len(s1)到len(s2)
        l = 0
        for r in range(len(s1), len(s2)):
            if match == 26: return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                match += 1
            elif s1Count[index] + 1 == s2Count[index]:
                match -= 1
            
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                match += 1
            elif s1Count[index] - 1 == s2Count[index]:
                match -= 1
            l += 1
        return match == 26