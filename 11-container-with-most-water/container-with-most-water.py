class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maxwater=0
        while(i<j):
            width=j-i
            height1=min(height[i],height[j])
            area=width*height1
            maxwater=max(maxwater,area)

            if (height[i]<height[j]):
                i+=1
            else:
                j-=1
        return maxwater