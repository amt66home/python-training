from functools import total_ordering


for item in 'Python':
    print(item)

for student in ['Mosh','John','Sarah']:
    print(student)

for item in [1,2,3,4]:
    print(item)

# the range function starts counting at zero
# this example prints the 10 numbers in the range ie 0-9
for item in range(10):
    print(item)

# this example prints the numbers in a range of 10 
# beginning with 5 ie 5-9
for item in range(5,10):
    print(item)

# this example prints the numbers in a range of 10
# starting at 5 and printing every 2nd number ie 5,7 and 9
# the 2 in it tells it the step size
for item in range(5,10,2):
    print(item)

prices = [10,20,30]
total = 0
for price in prices:
    total += price
#print(total)
print(f"total: {total}")

