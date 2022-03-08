command = ""

while True:
    command = input("> ").lower # take the input, convert to lowercase and store in command
    if command == "start":
        print("Car started ready to go")
    elif command == "stop":
        print("Car has stopped")
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit 
        """)
    elif command == "quit":
        break
else:
    print("I don't understand that")

# got to 1.37.40