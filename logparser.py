# import time and regex

import time
from time import strftime
import re

#i/o for operations
log_file_path = r"C:\Windows\Temp\tomcat.log"
export_file_path = r"C:\Windows\Temp"

#setting the time to a readable string 
atime = str(strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))

#create export file and full path 
file = "\\" + "Parser Output " + atime + ".txt"
export_file = export_file_path + file

#regex 
regex = '(DEBUG.*)'

#if read_line is true we step through the file line by line
#otherwise we'll just file.read the whole thing
read_line = True

#open the log as read only
#define match_list array
#iterate through each line of the file, matching the regex
#print to console and append the match_list with regex match
with open(log_file_path, "r") as file:
    match_list = []
    if read_line == True:
        for line in file:
            for match in re.finditer(regex, line, re.S):
                match_text = match.group()
                match_list.append(match_text)
                print(match_text)
    else:
        data = file.read()
        for match in re.finditer(regex, data, re.S):
            match_text = match.group();
            match_list.append(match_text)
file.close()

#open the export file with write access
#create a clean version of the match using list()
#iterate through the match list and write to file
with open(export_file, "w+") as file:
    file.write("EXPORTED DATA:\n")
    match_list_clean = list(set(match_list))
    length = len(match_list_clean)
    for item in range(length):
        print(match_list_clean[item])
        file.write(match_list_clean[item] + "\n")
file.close()
