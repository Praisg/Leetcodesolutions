1
class Solution:
2
    def rotatedDigits(self, n: int) -> int:
3
        def goodD(i):
4
            return ("2" in str(i) or "5" in str(i) or "6" in str(i) or "9" in str(i)) and ("3" not in str(i) and "4" not in str(i) and "7" not in str(i))
5
        
6
        count = 0
7
        for i in range(1 , n+1):
8
            if goodD(i) == True:
9
                count += 1
10
        return count        