#Command Line Input

import psutil
import sys
import os

def CreateLog(FolderName):

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret==True):
        Ret = os.path.isdir(FolderName)
        if(Ret == False):
            print("Unable to Create Folder :/")
            return
    
    else:
        os.mkdir(FolderName)
        print("Directory For Log Files Created successfully!!!!!")

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)

def main():
    Border = "-"*50
    print(Border)
    print("---- Marvellous Platform Surveillence System -----")
    print(Border)
    
    if (len(sys.argv) ==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Script is used to ")
            print("1: Create Automatic Logs")
            print("2: Executes Periodically")
            print("3: Sends mail with the Log")
            print("4: Print Information about Processess")
            print("5: Store information about CPU")
            print("6: Store information about RAM")
            print("7: Store information about Storage")

        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Use the Automation script as ")
            print("ScriptName.py TimeInterval DirectoryName")
            print("Time Interval: The time in minutes for peroiocic scheduling ")
            print("Directory Name: Name of the Directory to create auto logs ")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more detailed!")

    #python Demo.py 5 Marvellous
    elif(len(sys.argv)==3):
        print("Inside Projetcs Logic")
        print("Time Interval: ",sys.argv[1])
        print("Directory name: ",sys.argv[2])
        CreateLog(sys.argv[2])

    else:
        print("Invalid Number of Command Line Arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more detailed!")

    print(Border)
    print("-------Thank you for using our script--------- :-)")
    print(Border)

if __name__=="__main__":
    main()
