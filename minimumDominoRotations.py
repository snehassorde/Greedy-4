# Time Complexity : O(2n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
import collections
from typing import List
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        hmap = collections.defaultdict(list)
        target = -1
        n = len(tops)

        for i in range(n):
            hmap[tops[i]] = hmap.get(tops[i], 0) + 1
            if hmap[tops[i]] >= n:
                target = tops[i]
                break
            hmap[bottoms[i]] = hmap.get(bottoms[i], 0) + 1
            if hmap[bottoms[i]] >= n:
                target = bottoms[i]
                break
        
        tRot = 0
        bRot = 0
        for i in range(0, n):
            if tops[i] != target and bottoms[i] != target:
                return -1
            if tops[i] != target:
                tRot+=1
            if bottoms[i] != target:
                bRot+=1
            
        return min(tRot, bRot)

#Approach 2:
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(target):
            tRot, bRot = 0, 0
            for i in range(len(tops)):
                if tops[i] != target and bottoms[i] != target:
                    return -1
                if tops[i] != target:
                    tRot+=1
                if bottoms[i] != target:
                    bRot+=1
            return min(tRot, bRot)

        result = check(tops[0])
        if result != -1:
            return result
        return check(bottoms[0])
