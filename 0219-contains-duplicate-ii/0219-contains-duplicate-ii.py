class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for idx, val in enumerate(nums):
            if val in hashmap:
                if idx - hashmap[val] <= k:
                    return True
            hashmap[val] = idx
        return False
