# Time Complexity : O(m*n)
# Space Complexity : O(m)
class Solution:
    def shortestWay(self, source, target):
        source_set = set(source)  # O(1)
        i = 0
        j = 0
        count = 1
        while j < len(target):
            tChar = target[j]  # target character
            if tChar not in source_set:
                return -1
            if source[i] == tChar:
                i += 1
                j += 1
                if j == len(target):
                    return count
            else:
                i += 1
            if i == len(source):
                i = 0
                count += 1

        return count

sc = Solution()
print(sc.shortestWay("abc", "abcbc"))

#Approach 2: using map
# Time Complexity : O(m+nlogk)
# Space Complexity : O(m)
import collections
class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        hmap = collections.defaultdict(list)
        for i in range(len(source)):
            c = source[i]
            if c not in hmap:
                hmap[c] = []
            hmap[c].append(i)

            count = 1
            sp =0 
            tp = 0

        def binarySearch(arr, target):
            left, right = 0, len(arr) - 1
            result = len(arr)
            while left <= right:
                mid = (left+right) // 2
                if arr[mid] >= target:
                    result = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return result

        while tp < len(target):
            tChar = target[tp]
            if tChar not in hmap:
                return -1
            li = hmap[tChar]
            k = binarySearch(li, sp)
            if k < 0:
                k = -k-1
            
            if k == len(li):
                count+=1
                sp = li[0]
            else:
                sp = li[k]
                sp+=1
                tp+=1

        return count

sc = Solution()
print(sc.shortestWay("abc", "abcbc"))
print(sc.shortestWay("xyz", "xzyxz"))