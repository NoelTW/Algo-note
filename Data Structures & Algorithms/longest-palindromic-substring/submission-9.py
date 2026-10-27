class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        ans = ""
        for i in range(n):
            # odd
            r = l = i
            while l >= 0 and r < n and s[r] == s[l]:
                if len(s[l: r + 1]) > len(ans):
                    ans = s[l: r + 1]
                l -= 1
                r += 1
            r = i + 1
            l = i
            while l >= 0 and r < n and s[r] == s[l]:
                if len(s[l: r + 1]) > len(ans):
                    ans = s[l: r + 1]
                l -= 1
                r += 1  
        return ans
