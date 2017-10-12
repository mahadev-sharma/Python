def choiceToNumber(choice):
    if choice == 1:
        print('mahadev')
    elif choice == 2:
        print('parixit')
    elif choice == 3:
         print('dhruv')
    else :
         print('please select choice from 1-3')
#choiceToNumber(30)

def numberToChoice(name):
    if name == 'mahadev':
        print(1)
    elif name == 'parixit':
        print(2)
    elif name == 'dhruv':
         print(3)
    else :
         print('please select name of brothers')
#numberToChoice('dhruverh')

#using dictionaries
def choice_to_number(choice1):         
     #winningPlaces ={'mahadev1':1,'parixit1':2,'dhruv1':3}         
     #return winningPlaces[choice]
     return{'mahadev1':1,'parixit1':2,'dhruv1':3}[choice1]
print(choice_to_number('dhruv1'))
#we can do reverse in dictionaries
