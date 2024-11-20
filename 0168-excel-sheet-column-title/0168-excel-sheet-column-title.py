class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0:
            columnNumber -= 1
            c = columnNumber % 26
            ans += chr(c + ord('A'))
            columnNumber //= 26
        return ans[::-1]