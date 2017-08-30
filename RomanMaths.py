#converting first roman numeral to decima

arg1 = input('Enter first roman numeral: ')

print()
arg2 = input('Enter second roman numeral: ')
print()
arg3 = input('Enter Maths operation for roman numeral: +/-* ')

#function to convert roman to decimal
def roman(arg):
    total1 = 0

    for i in arg:
        if i == 'I':
            total1 += 1 
        elif i == 'V':
            total1 += 5
        elif i == 'X':
            total1 += 10
        elif i == 'L':
            total1 += 50
        elif i == 'C':
            total1 += 100
    if 'IV' in arg:
        total1 -= 2 
    if 'IX' in arg:
        total1 -= 2 
    if 'XL' in arg:
        total1 -= 20
    return total1

# converting from decimal to roman numeral  
def convert(arg):
    numeral = []      
    # splits the number into integers and appends roman numeral characters to a list 
    while arg > 1:
        for i in range(len(str(arg))): #this loop to identify the one, tens, hundreds place
            if i == 0:
                digit = arg % 10 
                arg //= 10
                if digit == 9:
                    numeral.append('IX')
                if 5 < digit < 9:
                    numeral.append('I' * (digit % 5))
                    digit -= digit % 5
                if digit == 5: 
                    numeral.append('V')
                if digit == 4: 
                    numeral.append('IV')
                if digit < 4: 
                    numeral.append('I' * digit)
            if i == 1:
                digit = arg % 10 
                arg //= 10
                if digit == 9:
                    numeral.append('XC')
                if 5 < digit < 9:
                    numeral.append('X' * (digit % 5))
                    digit -= digit % 5
                if digit == 5: 
                    numeral.append('L')
                if digit == 4: 
                    numeral.append('XL')
                if digit < 4: 
                    numeral.append('X' * digit) 
            if i == 2:
                digit = arg % 10
                arg //= arg
                numeral.append('C' * digit)
    numeral.reverse()#roman to be at index 0
    return numeral#passing only roman char

#converting arguments to decimal before any mathematical operations
arg1 = roman(arg1)
arg2 = roman(arg2)

# define the function blocks
def add():
    print( "You typed addition.")
    sum1 = arg1 + arg2
    res = convert(sum1)
    print( "addition is", ''.join(res))

def div():
    print( "You typed divsion ")
    div1 = arg1 // arg2
    res = convert(div1)
    print( "divison is", ''.join(res))
    

def sub():
    print( "You typed substraction ")
    sub1 = arg1 - arg2
    res = convert(sub1)
    print( "substraction is", ''.join(res))

def mul():
    print( "You typed multiplication ")
    mul1 = arg1 * arg2
    res = convert(mul1)
    print( "multiplication is", ''.join(res))

#creating dicionary
# map the inputs to the function blocks
operation = {'+' : add,
           '/' : div,
           '-' : sub,
           '*' : mul,
            }

result = operation[arg3]()