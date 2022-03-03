# If statements
is_hot = False
is_cold = True

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
 
print("Enjoy your day")

# Logical Operators
good_credit = True
bad_credit = False
price = 1000000.0

if good_credit:
    donwpayment = price * 0.1
    print(f"Down payment: {donwpayment}")
elif bad_credit:
    donwpayment = price * 0.2
    print(f"Down payment: {donwpayment}")
else:
    print("Credit check not complete")

has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:
    print("Eligible for good loan")

if has_high_income or has_good_credit:
    print("Eligible for average loan")

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for a loan")

# Comparison Operators
temp = 30

if temp > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")


name = input("What is your name")
if len(name) < 3 or len(name) > 50:
    print("Name must be a minimum of 3 characters and maximum of 50 characters")
else:
    print("Name looks good")
