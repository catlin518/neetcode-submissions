class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #1.先设置成set，把重复的剔除掉
        num_set = set(nums)
        res = 0
        
        #2.找到开头
        for num in num_set:
            if num - 1 not in num_set:
                current = num
                current_length = 1
                print(current)
                #3.往下找下一个代码
                while current + 1 in num_set:
                    current += 1
                    current_length += 1
                res = max(res, current_length)
        return res