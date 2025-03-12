# EXERCISE #3: ODD & EVEN

# isOdd(13)  →  True 
# isEven(13)  →  False

def isOdd(number):
    # Return whether number mod 2 is 1
    return number % 2 == 1

def isEven(number):
    # Return whether number mod 2 is 0
    return number % 2 == 0
    
print(isOdd(41) == False)
print(isOdd(42) == False)
print(isOdd(9999) == True)
print(isOdd(-10) == False)
print(isOdd(-11) == True)
print(isOdd(3.1415) == False)
print(isEven(42) == True)
print(isEven(9999) == False)
print(isEven(-10) == True)
print(isEven(-11) == False)
print(isEven(3.1415) == False)

