count =0
for number in range(1,4):
    count = count+number
print(count)



#write a function that sums all elements of a list and returns them
def sumList(myList):
    count1 =0
    for number1 in myList:
        count1 = count1 + number1
    print(count1)
    return count1        
assert sumList([1,2,3]) == 6
