class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #1.two pointer
        # l, r = 0, len(numbers) - 1

        # while l<r:
        #     curNum = numbers[l] + numbers[r]
        #     if curNum < target:
        #         l += 1
        #     elif curNum > target:
        #         r -= 1
        #     else:
        #         return [l+1, r+1]
        # return []

        #2.two sum(hash table)
        seen = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in seen:
                return [seen[complement] + 1, i + 1]
            seen[num] = i
        return []
