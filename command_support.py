import re
import os
import datetime
import webbrowser
import subprocess

#function to clear screen
def cls():
    os.system('cls')

#main function for commands support
def recognizeCommand(command):
    status = "ERROR: invalid command"

    #DISPLAY DATE
    if (re.search("[dD][aA][tT][eE]", command) or re.search("[dD][aA][yY]", command)):
        now = datetime.datetime.now()
        status = "SUCCESS: Today is: " + str(now.day) + "-" + str(now.month) + "-" + str(now.year)
        return status

    #DISPLAY TIME
    elif re.search("[tT][iI][mM][eE]", command):
        now = datetime.datetime.now()
        status = "SUCCESS: The time is: " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        return status

    #HANDLE OPENING COMMAND WITHOUTH FILENAME
    #elif (re.search("[oO][pP][eE][nN] [tT]*[eE]*[xX]*[tT]*[ ]*[fF][iI][lL][eE]$", command) or re.search("[rR][eE][aA][dD] [tT]*[eE]*[xX]*[tT]*[ ]*[fF][iI][lL][eE]$", command)):
        #status = "ERROR: no filename given"
        #return status

    #READ TEXT FILE
    elif (re.search("[oO][pP][eE][nN] [tT][eE][xX][tT][ ]*[fF][iI][lL][eE]", command) or re.search("[rR][eE][aA][dD] [tT][eE][xX][tT][ ]*[fF][iI][lL][eE]", command)):
        match = re.search("[tT]*[eE]*[xX]*[tT]*[ ]*[fF][iI][lL][eE] ([a-zA-Z0-9\-\_]+)", command)
        fileName = match.group(1)
        if not re.search("\.txt", fileName):
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

    #READ ANY FILE
    elif (re.search("[oO][pP][eE][nN] ([a-zA-Z0-9\-\_ ]*)[fF][iI][lL][eE]", command) or re.search("[sS][hH][oO][wW] ([a-zA-Z0-9\-\_ ]*)[fF][iI][lL][eE]", command)):
        print("Enter complete path to file:")
        filePath = input()
        filePath = filePath.replace("\\", "/")
        print("Enter complete path to program which can open this file:")
        programPath = input()
        programPath = programPath.replace("\\", "/")
        executeCommand = programPath + " " + filePath
        try:
            subprocess.call(executeCommand)
            status = "SUCCESS: file " + filePath + " opened with program " + programPath
        except:
            status = "ERROR: could not open file"
        return status

    #CREATE TEXT FILE
    elif re.search("[cC][rR][eE][aA][tT][eE] [tT][eE][xX][tT][ ]*[fF][iI][lL][eE]", command):
        print("Enter file name")
        fileName = input()
        file = open(fileName, 'a+')
        file.close()
        status = "SUCCESS: file \"" + fileName + "\" created"
        return status

    #OPEN WEB BROWSER
    elif (re.search("[oO][pP][eE][nN] [wW]*[eE]*[bB]*[ ]*[bB][rR][oO][wW][sS][eE][rR]", command) or re.search("[oO][pP][eE][nN] [iI][nN][tt][eE][rR][nN][eE][tT]", command)):
        match = re.search(r"[pP][aA][gG][eE] ([a-zA-Z0-9\.\-\_\/]+)", command)
        #print(match.group(1))
        pageUrl = match.group(1)
        webbrowser.open_new_tab(pageUrl)
        status = "SUCCESS: opened web browser with page " + pageUrl
        return status

    #SHIPS
    elif re.search("run random program", command):
        print("Are you sure? It will close Human Console")
        print("Type \"yes\" or \"no\"")
        shipsChoice = input()
        if shipsChoice == "yes":
            try:
                subprocess.run("python ships.py")
                status = "SUCCESS: ships played"
                return status
            except:
                status = "ERROR: could not run ships game"
                return status
        else:
            status = "ERROR: user don\'t want to play ships"
            return status

    #RUN OTHER PROGRAM
    elif re.search("[rR][uU][nN]", command):
        if re.search("[rR][uU][nN][ ]*[pP]*[rR]*[oO]*[gG]*[rR]*[aA]*[mM]* ([a-zA-Z0-9\.\_\-\/]+)", command):
            match = re.search("[rR][uU][nN][ ]*[pP]*[rR]*[oO]*[gG]*[rR]*[aA]*[mM]* ([a-zA-Z0-9\.\_\-\/]+)", command)
            programName = match.group(1)
            programName = programName.replace("\\", "/")
            try:
                subprocess.call(programName)
                #os.system(programName)
                status = "SUCCESS: started program " + programName
            except:
                status = "ERROR: could not run program"
            return status
        else:
            print("Enter whole path to program:")
            programPath = input()
            try:
                subprocess.call(programPath)
                status = "SUCCESS: started program " + programPath
            except:
                status = "ERROR: could not run program"
            return status

    #CLOSE OTHER PROGRAM
    elif (re.search("[kK][iI][lL][lL] [pP]*[rR]*[oO]*[gG]*[rR]*[aA]*[mM]*", command) or re.search("[cC][lL][oO][sS][eE] [pP]*[rR]*[oO]*[gG]*[rR]*[aA]*[mM]*", command)):
        if re.search("[kK][iI][lL][lL] [pP][rR][oO][gG][rR][aA][mM]+ ([a-zA-Z0-9\-\_\.]+)", command):
            match = re.search("[kK][iI][lL][lL] [pP][rR][oO][gG][rR][aA][mM]+ ([a-zA-Z0-9\-\_\.]+)", command)
            programName = match.group(1)
            if re.search(".exe", programName):
                killCommand = "taskkill /f /im " + programName
                subprocess.call(killCommand)
                status = "SUCCESS: Process " + programName + " terminated"
                return status
            else:
                programName += ".exe"
                killCommand = "taskkill /f /im " + programName
                subprocess.call(killCommand)
                status = "SUCCESS: Process " + programName + " terminated"
                return status
        elif re.search("[kK][iI][lL][lL] ([a-zA-Z0-9\-\_\.]+)", command):
            match = re.search("[kK][iI][lL][lL] ([a-zA-Z0-9\-\_\.]+)", command)
            programName = match.group(1)
            if re.search(".exe", programName):
                killCommand = "taskkill /f /im " + programName
                subprocess.call(killCommand)
                status = "SUCCESS: Process " + programName + " terminated"
                return status
            else:
                programName += ".exe"
                killCommand = "taskkill /f /im " + programName
                subprocess.call(killCommand)
                status = "SUCCESS: Process " + programName + " terminated"
                return status
        elif re.search("[cC][lL][oO][sS][eE] [pP][rR][oO][gG][rR][aA][mM]+ ([a-zA-Z0-9\-\_\.]+)", command):
            match = re.search("[cC][lL][oO][sS][eE] [pP][rR][oO][gG][rR][aA][mM]+ ([a-zA-Z0-9\-\_\.]+)", command)
            programName = match.group(1)
            if re.search(".exe", programName):
                killCommand = "taskkill /f /im " + programName
                subprocess.call(killCommand)
                status = "SUCCESS: Process " + programName + " terminated"
                return status
            else:
                programName += ".exe"
                killCommand = "taskkill /f /im " + programName
                subprocess.call(killCommand)
                status = "SUCCESS: Process " + programName + " terminated"
                return status
        elif re.search("[cC][lL][oO][sS][eE] ([a-zA-Z0-9\-\_\.]+)", command):
            match = re.search("[cC][lL][oO][sS][eE] ([a-zA-Z0-9\-\_\.]+)", command)
            programName = match.group(1)
            if re.search(".exe", programName):
                killCommand = "taskkill /f /im " + programName
                subprocess.call(killCommand)
                status = "SUCCESS: Process " + programName + " terminated"
                return status
            else:
                programName += ".exe"
                killCommand = "taskkill /f /im " + programName
                subprocess.call(killCommand)
                status = "SUCCESS: Process " + programName + " terminated"
                return status

    #PRINT LIST OF ITEMS IN DIRECTORY
    elif (re.search("[sS][hH][oO][wW] ([a-zA-Z0-9\-\_\. ]+)[dD][iI][rR][eE]*[cC]*[tT]*[oO]*[rR]*[yY]*", command) or re.search("[lL][iI][sS][tT] ([a-zA-Z0-9\-\_\. ]*)[dD][iI][rR][eE]*[cC]*[tT]*[oO]*[rR]*[yY]*", command)):
        match = re.search("[dD][iI][rR][eE]*[cC]*[tT]*[oO]*[rR]*[yY]* ([a-zA-Z0-9\-\_\.\:\/]+)$", command)
        path = match.group(1)
        list = str(os.listdir(path))
        status = "SUCCESS: list of files in directory \"" + path + "\":\n" + list
        return status

    #ASR
    elif re.search("[aA][sS][rR]", command):
        status = "SUCCESS: ASR works correctly"
        return status

    return status
