#find the biggest numbr among three numbers
def biggestGuy (num1,num2,num3):
    if ((num1 > num2) and (num1 > num3)) :
        print('number 1 is the biggest number among them')
    elif ((num2 > num1) and (num2 > num3)) :
        print('number 2 is the biggest number among them')
    elif ((num3 > num2) and (num3 > num1)) :
        print('number 3 is the biggest number among them')
    else:
        print('any two or all three numbers are equal')
biggestGuy(1,1,1)        
