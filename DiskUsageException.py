#Command Line Input

import psutil
import sys
import os
import time
import schedule

def CreateLog(FolderName):
    Border = "-"*50
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

    timeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    FileName = os.path.join(FolderName,"Marvellous_%s.log"%timeStamp)
    print("Log Files gets Created with name: ",FileName)

    fobj = open(FileName,"w")

    fobj.write(Border+"\n")
    fobj.write("---- Marvellous Platform Surveillence System -----\n")
    fobj.write("Log Created at: "+time.ctime()+"\n")
    fobj.write(Border+"\n")

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    fobj.write(Border+Border+"\n")
    fobj.write("-------------End of Log File-----------------")
    fobj.write(Border+Border+"\n")

    print("CPU Usage: ",psutil.cpu_percent())

    mem = psutil.virtual_memory()
    print("RAM usage: ",mem.percent)

    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            print(f"{part.mountpoint} used {usage.percent}%%")
        except:
            pass
    
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
        
        #Apply the Schedular
        schedule.every(int(sys.argv[1])).minutes.do(CreateLog,sys.argv[2])
        print("Platform Surveillence System started successfully!!!!!!")
        print("Directory Created with name: ",sys.argv[2])
        print("Time Interval in Minutes : ",sys.argv[1])
        print("Press Ctrl + C to stop the execution")
        #Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid Number of Command Line Arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more detailed!")

    print(Border)
    print("-------Thank you for using our script--------- :-)")
    print(Border)

if __name__=="__main__":
    main()
