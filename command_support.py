import re
import sys
import os
import datetime
import webbrowser
import subprocess

#function to clear screen
def cls():
    os.system('cls')

#main function for commands support
def recognizeCommand(command):
    status = "invalid command"

    #DISPLAY DATE
    if re.search("[dD][aA][tT][eE]", command):
        now = datetime.datetime.now()
        status = "SUCCESS: Today is: " + str(now.day) + "-" + str(now.month) + "-" + str(now.year)
        return status

    #DISPLAY TIME
    if re.search("[tT][iI][mM][eE]", command):
        now = datetime.datetime.now()
        status = "SUCCESS: The time is: " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        return status

    #HANDLE OPENING COMMAND WITHOUTH FILENAME
    if re.search("[oO][pP][eE][nN] [tT]*[eE]*[xX]*[tT]*[ ]*[fF][iI][lL][eE]", command):
        status = "ERROR: no filename given"
        return status

    #READ TEXT FILE
    if (re.search("[oO][pP][eE][nN] [tT]*[eE]*[xX]*[tT]*[ ]*[fF][iI][lL][eE] ([a-zA-Z0-9\-_]+)", command) or re.search("[rR][eE][aA][dD] [tT]*[eE]*[xX]*[tT]*[ ]*[fF][iI][lL][eE] ([a-zA-Z0-9\-_]+)", command)):
        match = re.search("[tT]*[eE]*[xX]*[tT]*[ ]*[fF][iI][lL][eE] ([a-zA-Z0-9\-\_]+)", command)
        fileName = match.group(1)
        fileName += ".txt"
        fileInput = "open"
        try:
            file = open(fileName, 'r')
            cls()
            for line in file:
                print(line)
            print("*************************************************************")
            print("Type anything to close this file")
            fileInput = input()

            status = "SUCCESS: file printed"
            file.close()
        except IOError:
            status = "ERROR: no access to file"
        except FileNotFoundError:
            status = "ERROR: file does not exist"
        except:
            status = "ERROR: unexpected error"
        return status

    #CREATE TEXT FILE
    if re.search("[cC][rR][eE][aA][tT][eE] [tT]*[eE]*[xX]*[tT]*[ ]*[fF][iI][lL][eE]", command):
        print("Enter file name")
        fileName = input()
        file = open(fileName, 'w+')
        file.close()
        status = "SUCCESS: file \"" + fileName + "\" created"
        return status

    #OPEN WEB BROWSER
    if (re.search("[oO][pP][eE][nN] [wW]*[eE]*[bB]*[ ]*[bB][rR][oO][wW][sS][eE][rR]", command) or re.search("[oO][pP][eE][nN] [iI][nN][tt][eE][rR][nN][eE][tT]", command)):
        match = re.search(r"[pP][aA][gG][eE] ([a-zA-Z0-9\.\-\_\/]+)", command)
        #print(match.group(1))
        pageUrl = match.group(1)
        webbrowser.open_new_tab(pageUrl)
        status = "SUCCESS: opened web browser with page " + pageUrl
        return status

    #RUN OTHER PROGRAM
    if re.search("[rR][uU][nN][ ]*[pP]*[rR]*[oO]*[gG]*[rR]*[aA]*[mM]*", command):
        match = re.search("[rR][uU][nN][ ]*[pP]*[rR]*[oO]*[gG]*[rR]*[aA]*[mM]* ([a-zA-Z0-9\.\_\-]+)", command)
        programName = match.group(1)
        subprocess.run(programName)
        #os.system(programName)
        status = "SUCCESS: started program " + programName
        return status

    #CLOSE OTHER PROGRAM


    return status
