class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic={}
        for ind, key in enumerate(nums):
            if key in dic and ind-dic[key]<=k:
                return True
            dic[key]=ind
        return False        
