def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k +=1
        
        return k

"""
Thought process:
Since we need to return the first k elements that are not equal to val, we will use k as a variable to keep track of the position within the array where we have to change the element that is not val.
1. Loop through the array and only change the element from the beginning of the list when a not val element has been found.
2. Increment k to fill in first k elements within the array.

Time complexity: O(n) since we looped through the array once
Space complexity: O(1) since we only used one variable
"""