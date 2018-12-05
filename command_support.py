import re
import sys
import os
import datetime

#main function for commands support
def recognizeCommand(command):
    status = "status"

    #DISPLAY DATE
    if re.match("date", command):
        now = datetime.datetime.now()
        status = "SUCCESS: Today is: " + str(now.day) + "-" + str(now.month) + "-" + str(now.year)

    #DISPLAY TIME
    if re.match("time", command):
        now = datetime.datetime.now()
        status = "SUCCESS: The time is: " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)

    return status
