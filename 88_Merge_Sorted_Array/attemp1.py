def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    if n != 0:
        if m == 0:
            nums1.clear()
            nums1.extend(nums2)
        else:
            mergeList = nums1[0:m]
            mergeList.extend(nums2)
            mergeList.sort()
            nums1.clear()
            nums1.extend(mergeList)

"""
Thought process:
1. I thought I had to iterate through each element one by one or make swaps between elements since it's an array, but then I remembered that Python has built in functions. 
2. Using the given example test cases, I have 3 conditions which are:
- if n == 0, do nothing, since we aren't returning anything. (1)
- if n != 0, merge both arrays. (3)
- if n != 0 and m == 0, copy nums2 into nums1 --> clearing nums1 and then extending nums2. (2)
3. Going by the step order, I used nested ifs when n != 0 and separate the cases where m == 0 and m != 0.

Since we definitely know that the first 0 to m-1 elements in nums1 are the m elements or not 0, we copy them into a new list, named mergeList, that will contain all the elements from nums1 and nums2. We then sort the mergeList before copying into nums1.

Time Complexity:  O((m+n)log(m+n))
Slice nums1[0:m] → O(m)
Extend with nums2 → O(n)
Sort → O((m+n) log(m+n)) ← this dominates
Clear → O(1) (amortized, but sometimes considered O(m+n) if it deallocates)
Extend again → O(m+n)
(I wasn't sure so I used chatgpt for time complexity)

Space complexity is O(m+n) since we created an array with m+n elements.
"""