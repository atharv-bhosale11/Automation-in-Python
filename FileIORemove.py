import os

def main():
    FileName = input("Enter tha Name of File: ")

    if os.path.exists(FileName):
        os.remove(FileName)
        print("----File Gets Deleted----")

    else:
        print("There is no such file")
        
if __name__=="__main__":
    main()
