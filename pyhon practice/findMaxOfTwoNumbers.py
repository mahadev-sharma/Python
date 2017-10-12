#find maximum number
'''def maxNumber(num1,num2):
    if num1 > num2 :
        print('first number is big')
    elif num2 > num1 :
        print('second number is big')
    else:
        print('both the numbers are equal')'''

def maxNumber(num1,num2):
    if num1 > num2 :
        return num1
    elif num2 > num1 :
       return num2
    else:
        print('both the numbers are equal')
maxNumber(110,10)
