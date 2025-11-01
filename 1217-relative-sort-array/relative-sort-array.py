class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        max_val=max(arr1)
        freq = [0] * (max_val + 1)

        for i in arr1:
            freq[i]+=1
        res=[]

        for i in arr2:
            while freq[i]>0:
                res.append(i)
                freq[i]-=1

        for num in range(len(freq)):
            while freq[num] > 0:
                res.append(num)
                freq[num] -= 1
        return res

        