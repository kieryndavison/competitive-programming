import collections
from typing import Collection


class Solution:
    # def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
    #     numsInA = {}
    #     numsInA = defaultdict(lambda: 0, numsInA)
    #     maxNum = max(target) if max(target) > max(arr) else max(arr)

    #     for i, num in enumerate(target):
    #         numsInA[num] += 1
    #         numsInA[arr[i]] -= 1

    #     return all(numsInA[key] == 0 for key in range(maxNum))
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return collections.Counter(target) == collections.Counter(arr)