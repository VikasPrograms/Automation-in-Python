
# ===================
#
# Imports
#
# ===================

import psutil
from sys import*

# ==============================
#
# Process Display Operation
#
# ==============================

def ProcessDisplay():
    print("List Of Running Processes")

    Data = [] # create list
    for proc in psutil.process_iter(): # process_iter is use for to Search all running processes on the local machine
        value = proc.as_dict(attrs = ['pid', 'name', 'username'])
        # as_dict method retrieving multiple process information as a dictionary,
        # attrs is attribute names, arrs shows list of possible string values as pid, ppid, name, username, memory_full_info
        Data.append(value)

    return Data
  
# =======================
#
# Entry Point
#
# =======================

def main():

    print("\n")
    print("------ Python Automation ------")
    print("---- Running Process Identifier ----")
    print("\n")
    
    print("Script Title : " + argv[0])

    arr = ProcessDisplay()

    for element in arr:
        print(element) # display all data using for loop
        
# =======================
#
# Code Starter
#
# =======================

if __name__ == "__main__":
    main()