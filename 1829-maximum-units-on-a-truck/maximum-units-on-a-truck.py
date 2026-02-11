class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sum1=0
        boxTypes.sort(key=lambda x: x[1], reverse=True)
     
             
        for i in range(len(boxTypes)):
            
            boxes = boxTypes[i][0]
            units = boxTypes[i][1]
            
            if truckSize == 0:
                break
            
            if boxes <= truckSize:
                sum1 += boxes * units
                truckSize -= boxes
            else:
                sum1 += truckSize * units
                truckSize = 0
        
        return sum1