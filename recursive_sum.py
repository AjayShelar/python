

"""https://www.geeksforgeeks.org/recursive-sum-digits-number-formed-repeated-appends/"""

"""Given two positive number N and X. The task is to find the sum of digits of a number formed by N repeating X number of times until sum become single digit.

Examples:

Input : N = 24, X = 3
Output : 9
Number formed after repeating 24 three time = 242424
Sum = 2 + 4 + 2 + 4 + 2 + 4
    = 18
Sum is not the single digit, so finding 
the sum of digits of 18,
1 + 8 = 9

Input : N = 4, X = 4
Output : 7
"""

def digSum(n):
 
    if (n == 0):
        return 0
    if (n % 9 == 0):
        return 9
    else:
        return (n % 9)
        
#times until sum become single digit.
def repeatedNumberSum(n, x):
    
    sum = x * digSum(n)
    
    return digSum(sum)

def main():

    n = 24
    x = 3
    print(repeatedNumberSum(n, x))
if __name__=="__main__":
    main()