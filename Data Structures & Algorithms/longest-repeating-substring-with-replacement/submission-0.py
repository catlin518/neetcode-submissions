class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #1.inital a dict
        count = {}
        l = 0
        maxf = 0
        res = 0 #maxlength


        for r in range(len(s)):
            #check(update) s[r] number in count
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            #
            while (r - l + 1) - maxf > k :
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
            
