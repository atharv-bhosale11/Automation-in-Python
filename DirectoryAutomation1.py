import os
import sys

def DirectoryScanner(DirName="Marvellous"):
    Ret = False

    Ret = os.path.exists(DirName)

    if Ret==False:
        print("There is No such Directory")
        return
    
    Ret = os.path.isdir(DirName)

    if Ret == False:
        print("It is not directory")
        return

    for FolderName,SubFolder,FileName in os.walk(DirName):
        for fname in FileName:
            print(fname)
          
def main():
    Border = "-"*52
    print(Border)
    print("---------------Marveelous Automation----------------")
    print(Border)

    if(len(sys.argv)!=2):
        print("Invalid number of arguments")
        print("Please!! Specify the Name of Directoru")
        return

    DirectoryScanner(sys.argv[1])
if __name__ == "__main__":
    main()
