firstName = 'John'
lastName = 'Smith'
message = firstName + ' [' + lastName + '] is a coder'
print(message)

# Using formatted strings instead makes it easier to visualise the output
# The curly braces are placehoders and will display the value of your variables

msg = f'{firstName} [{lastName}] is a coder'
print(msg)

msg1 = f'{firstName} {lastName} is a coder'
print(msg1)