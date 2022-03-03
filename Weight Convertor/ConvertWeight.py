
unit = input("Enter L for lbs or K for kg?")
weight = int(input("Enter your weight"))

if unit.upper() == 'L':
    converted = weight * 0.45
    print(f"You are {converted} kg")
else:
    converted = weight / 0.45
    print(f"You are {converted} lbs")

