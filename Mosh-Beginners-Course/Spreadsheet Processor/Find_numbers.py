import re

# Target string
target_string = "The old house where the old man lived was rundown"
target_string2 = "The numbers are 1 - 20 and 17, 22, 25, 35, 45, 3, 26, 9"

# find substring 'old'
result = re.search(r"old", target_string)

# print matching substring
print("The word found was - " + result.group())

# find all numbers in a string
second_result = re.findall(r"\d+", target_string2)

# print all matches
print("Found the following matches")
print(second_result)