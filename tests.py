class Solution:
    @staticmethod
    def is_palindrome(x: int) -> bool:
        str_x = str(x)
        backwards = []

        for i in range(len(str_x)-1, -1, -1):
            backwards.append(str_x[i])

        if ''.join(backwards) == str_x:
            return True
        return False


s1 = Solution()
print(s1.is_palindrome(121))
