import sys
import os
import speech_text as st
import command_support as cs

#t = st.getSpeechCommand()
#print(t) #{'success': True, 'error': None, 'transcription': 'hello and welcome my friend'}

#function to clear screen
def cls():
    os.system('cls')


choice = '0'
command = "command"
status = "program is running"
validCommand = True
commandsHistory = [] #list of previous commands
statusHistory = [] #list of status of previous commands
history = 0

while (choice != '4'):
    cls()
    print("*************************************************************")
    print("Welcome to Human Console, please start by choosing an option:")
    print("1: write command")
    print("2: say command")
    print("3: enter commands history")
    print("4: exit Human Console")
    if (history > 0):
        print("*************************************************************")
        print("Command history:") #last 3 commands
        print("...")
        if (history == 1):
            print(commandsHistory[0])
            print(statusHistory[0])

        if (history == 2):
            print(commandsHistory[0])
            print(statusHistory[0])
            print(commandsHistory[1])
            print(statusHistory[1])

        if (history > 2):
            x = len(commandsHistory)
            for i in range(x-3, x):
                print(commandsHistory[i])
                print(statusHistory[i])

    print("*************************************************************")
    print("Enter your actual choice here:")
    choice = input()

    #text input
    if (choice == '1'):
        print("Enter your command:")
        command = input()
        validCommand = True

    #speech input
    if (choice == '2'):
        response = st.getSpeechCommand()
        if (response["success"] == True):
            command = response["transcription"]
            validCommand = True
        if (response["success"] == False):
            command = "NULL"
            status = "Error: " + response["error"]
            validCommand = False

    #if speech was succesfully transcripted into text
    if (validCommand == True):
        history += 1
        commandsHistory.append(command)

        #trying to understand the command
        status = cs.recognizeCommand(command)

        s = "Status: " + status
        statusHistory.append(s)


    if (choice == '3'):
        historyInput = ""
        while (historyInput != "exit"):
            cls()
            size = len(commandsHistory) - 1
            for i in range(0, size):
                print("Command number: ", i + 1)
                print(commandsHistory[i])
                print(statusHistory[i])
            print("*************************************************************")
            print("Total number of commands: ", size)
            print("Type \"save\" to save commands history to file")
            print("Type \"exit\" to exit commands history")
            historyInput = input()
            if (historyInput == "save"):
                #save history to file
                historyFile = open("history.txt", "w+")
                for i in range(0, size):
                    historyFile.write(commandsHistory[i] + "\n")
                    historyFile.write(statusHistory[i] + "\n")
                historyFile.close()

    '''
    if (choice > '4' or choice < '1'):
        print("Invalid choice number")
    '''

print("Goodbye")
