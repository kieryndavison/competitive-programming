class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:        
        for i, source, target in sorted(zip(indices, sources, targets), reverse=True):
            if s[i:i + len(source)] == source:
                s = s[:i] + target + s[i+len(source):]
        return s