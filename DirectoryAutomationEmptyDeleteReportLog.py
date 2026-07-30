import os
import sys

def DirectoryScanner(DirName="Atharv"):
    Border = "-"*52
    fobj = open("Data.log","w")

    fobj.write(Border +"\n")
    fobj.write("This is a log file created by Atharv's Automation\n")
    fobj.write("This is Directory Cleaner Script\n")
    fobj.write(Border +"\n")
    Ret = False

    Ret = os.path.exists(DirName)

    if Ret==False:
        print("There is No such Directory")
        return
    
    Ret = os.path.isdir(DirName)

    if Ret == False:
        print("It is not directory")
        return

    FileCount = 0
    EmptyFileCount = 0

    for FolderName,SubFolder,FileName in os.walk(DirName):

        for fname in FileName:
            FileCount = FileCount + 1
            fname=os.path.join(FolderName,fname)
            
            if(os.path.getsize(fname)==0):      #empty file
                EmptyFileCount = EmptyFileCount + 1
                os.remove(fname)
    
    Border = "-"*52
    fobj.write(Border +"\n")

    fobj.write("Total File Scanned: "+str(FileCount)+"\n")
    
    fobj.write("Total EmptyFile Counts: "+str(EmptyFileCount)+"\n")
    fobj.write(Border +"\n")

    fobj.close()

def main():
    Border = "-"*52
    print(Border)
    print("---------------Atharv's Automation----------------")
    print(Border)

    if(len(sys.argv)!=2):
        print("Invalid number of arguments")
        print("Please!! Specify the Name of Directoru")
        return

    DirectoryScanner(sys.argv[1])

    print(Border)
    print("---------------Atharv's Automation----------------")
    print(Border)
  
if __name__ == "__main__":
    main()
