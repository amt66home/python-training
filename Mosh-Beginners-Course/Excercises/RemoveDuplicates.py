numbers = [5,5,7, 7,5,2, 1, 7, 4]
uniques =[]
print(numbers)
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)


