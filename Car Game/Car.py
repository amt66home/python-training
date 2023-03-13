car_cmd = ""
started = False

while True:
    car_cmd = input(">  ").lower()
    if car_cmd == "start":
        if started:
            print ("Car is already started")
        else:
            started = True
            print("Car started")
    elif car_cmd == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Car stopped")
    elif car_cmd == "quit":
        break
    elif car_cmd == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    else:
        print("I don't understand that")