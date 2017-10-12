#square number in list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

squared_numbers = []

for number in numbers:
  squared_numbers.append(number ** 2)
  
print(squared_numbers)


numbers1 = [1, 5, 2, 6, 3, 28, 27, 54, 3]  # ==> 129

result = 0

for number1 in numbers1:
  result = result + number1
  
print(result)
