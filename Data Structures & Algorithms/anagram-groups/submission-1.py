class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_fingerprint(word):
            fingerprint = ''.join(sorted(word))
            return fingerprint
        
        group = defaultdict(list)
        for s in strs:
            fingerprint = get_fingerprint(s)
            group[fingerprint].append(s)
        return list(group.values())
        