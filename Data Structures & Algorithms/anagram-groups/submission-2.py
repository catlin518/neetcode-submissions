class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_fingerprint(word):
            #1.sort排序 时间复杂度n*klogk
            # fingerprint = ''.join(sorted(word))
            # return fingerprint

            #2.数组的形式
            for char in word:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            return key
            

        
        group = defaultdict(list)
        for s in strs:
            count = [0] * 26
            fingerprint = get_fingerprint(s)
            group[fingerprint].append(s)
        return list(group.values())
        