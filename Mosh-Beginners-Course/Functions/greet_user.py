def greet_user(f_name, last_name):
    print(f'Hi {f_name} {last_name}!')
    print('Welcome aboard')


print("Start")
greet_user("John","Smith")
print("Finish")

# you can use key word arguments instead of positional arguments

print("start")
greet_user(last_name="Smith", f_name="John")
print("Finish")

# if using positional and keyword arguements, the positional one must come first
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')

print("start")
greet_user("Smith", first_name="Bill")
print("Finish")