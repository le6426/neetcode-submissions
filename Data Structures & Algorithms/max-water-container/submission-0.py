class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftPointer = 0
        rightPointer = len(heights) - 1
        largest = 0

        while leftPointer < rightPointer:

            if heights[leftPointer] > heights[rightPointer]:
                current = heights[rightPointer] * (rightPointer - leftPointer)
                rightPointer -= 1
            else:
                current = heights[leftPointer] * (rightPointer - leftPointer)
                leftPointer += 1

            largest = max(largest, current)
        
        return largest