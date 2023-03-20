# for storing key value pairs
# each key should be unique
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])

# If you pass a key in that doesn't exist (it's case sensitive) you
# get an error.  To avoid this use a getter, it will return 'none' if 
# you pass an invalid key
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer.get("birthdate"))

# You can supply a default value so if the key doesn't exist it will
# assign a default value to it:
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer.get("birthdate","1 Jan 1980"))

# You can change the value of a key value pair
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["name"] = "Jack Smith"
print(customer["name"])

# You can add a key pair:
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
customer["birthdate"] = "20 Jan 1980"
print(customer["birthdate"])

# Excercise, take someones phone number and print it as words
# eg 123 would be one two three:
phone = input("Phone: ")
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch,"!") + " "
print(output)






