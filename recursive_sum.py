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