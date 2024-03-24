# delete files with old at then of the name
import re
import glob

# Target string
filelist = glob.glob('.xlsx')
target_string = "The old house where the old man lived was rundown"
target_string2 = "The numbers are 1 - 20 and 17, 22, 25, 35, 45, 3, 26, 9"

# find substring 'old'
result = re.search(r"old", target_string)

# print matching substring
print(result.group())

# find all numbers in a string
second_result = re.findall(r"\d+", target_string2)

# print all matches
print("Found the following matches")
print(second_result)
