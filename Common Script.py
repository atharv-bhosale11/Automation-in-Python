import sys
import os
import time
import schedule

def fun(DirName):
    pass

def main():

    Border  = "-"*50
    print(Border)
    print("-----Data Shield System------")
    print(Border)

    if (len(sys.argv) == 2):
        if (sys.argv[1] == "--h" or  sys.argv[1] == "--H"):
            print("This script is used to ")
            print("1.Text AutoBackup at a given time")
            print("2.Backup only new and updated files")
            print("3. Create and Archieve(Zip) of the Backup Periodically")

        elif (sys.argv[1] == "--u" or  sys.argv[1] == "--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval: The time in minutes for periodic Scheduling")
            print("SourceDirectory : Name of Directory to backed up")
            
        else :
            print("Unable to proceed as there is no such option")
            print("Please use --h or --u to get more details ")

    # Python Demo.py 5 Data 
    elif(len(sys.argv) == 3):
        print("Inside project logic")
        print("Time interval : ",sys.argv[1])
        print("Directory Name : ",sys.argv[2])

        #Apply the scheduler

        schedule.every(int(sys.argv[1])).minutes.do(fun, sys.argv[2])

        print("Data Shield System started succesfully")
        print("Time Interval in minutes :",sys.argv[1])   
        print("Press CTRL + C to stop the execution") 
        
        
        # Wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)


    else:
        print("Invalid number of commad line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details ")


    print(Border)
    print("----------Thank you for using our script----------")
    print(Border)

if __name__ == "__main__":
    main()
