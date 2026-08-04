def main():

    try:
        fobj = open("Hello.txt","r")
        print("File gets successfully opend!!!!!")

        print("Current Offset is: ",fobj.tell())

        Data = fobj.read(6)
        
        print("Current Offset is: ",fobj.tell())

        print("Data from the file is: ",Data)
        
        fobj.close()
        
    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of Application")
        
if __name__=="__main__":
    main()

