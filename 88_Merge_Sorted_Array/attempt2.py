def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        midx = m - 1
        nidx = n - 1
        curr = m + n - 1 # update nums1 from the back

        while nidx >= 0:
            # if midx is valid and nums1[midx] > nums2[nidx], copy nums1[midx] to nums1[curr]
            # else copy nums2[nidx] to nums1[curr]
            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[curr] = nums1[midx]
                midx -= 1
            else:
                nums1[curr] = nums2[nidx]
                nidx -= 1
            
            curr -= 1


"""
Thought process:
1. We know that both arrays are sorted in non-decreasing order. We can use this property to our advantage by merging from the back of nums1.
2. We compare the last elements of both arrays and place the larger one at the end of nums1. 
3. We then move the pointer of the array from which we took the element one step back.
4. We repeat this process until we have processed all elements from both arrays.

Time Complexity: O(m + n) because we are iterating through both arrays once.
Space Complexity: O(1) because we are only creating variables as indices of the arrays
""" 