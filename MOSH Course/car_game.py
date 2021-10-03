help = '''

start - start the car 

stop = stop the car 

quit = quit the program 

'''
command = ""
started = False
while True:

    command = input(">")
    if command == "start":
        if started:
            print("car has started already!")
        else:
            print("Car started ")
            started = True
    elif command == "help":
        print(help)
    elif command == "stop":
        if started:
            print("Car stopped")
            started = False
        else:
            print("car has stopped already!")
    elif command == "quit":
        break


