1
class Solution:
2
    def majorityElement(self, nums: List[int]) -> List[int]:
3
        h = {}
4
        for i in nums:
5
            if i in h:
6
                h[i] += 1
7
            else:
8
                h[i] = 1
9
        print(h)        
10
            
11
        s = set()
12
        for i in nums:
13
            if h[i] > len(nums)//3: 
14
                s.add(i)
15
        return list(s)