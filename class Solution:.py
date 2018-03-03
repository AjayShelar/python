
"""Determine whether an integer is a palindrome. Do this without extra space."""
"""https://leetcode.com/problems/palindrome-number/description/"""

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
             return False
        
        elif x > 0:
            
            div = 1
            while x / div >= 10:
                div *= 10;


            while x != 0:
#                 print( int(x / div),int(x % 10))
                l = int(x / div)
                r = int(x % 10)
                if l != r:
                    return False
                x = (x % div) / 10
                div /= 100

                return True

def main():
    
    solution = Solution()        
    print(solution.isPalindrome(-2147483648))

if __name__ == '__main__':
    main()