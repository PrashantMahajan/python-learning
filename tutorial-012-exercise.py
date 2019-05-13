#https://youtu.be/_uQrJ0TkZlc?t=5469
programRun = True;
lastCommand = "";
while programRun:
    command = input(">").lower();
    if 'help' == command:
        print('''
Please Use the Following Commands:
Start : To start the car
Stop : To stop the car
Quit : to Quit the Game
        ''');
    elif 'start' == command:
        if 'start' == lastCommand:
            print('Car Is Already running');
        else:
            print('Car started - Gr..Gr')
    elif 'stop' == command:
            if 'stop' == lastCommand:
                print('Car is Already Stopped');
            else:
                print('Car stopped - :(')
    elif 'quit' == command:
        print('Quitting the Game')
        programRun = False;
    else:
        print("Command Not Found");
    lastCommand = command;
else:
    print('Game Finished successfully')