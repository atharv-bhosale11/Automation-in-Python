import sys
def main():
    Border = "-"*52
    print(Border)
    print("----------------Marvellous Automation---------------")
    print(Border)

    if (len(sys.argv)==2):
        if((sys.argv[1]=="--h")or sys.argv[1]=="--H"):
            print("This application is used to perform ________________")
            print("This is automation script")

        elif((sys.argv[1]=="--u")or sys.argv[1]=="--U"):
            print("Use the given script as ")
            print("ScriptName.py_Argument 1 Argument 2")
            print("Argument 1: ___________")
            print("Argument 2: ___________")
  
        else:
            print("Use the given flags as :" )
            print("--u: used to displauy the usage ")
            print("--h: used to display the help")
    else:
        
        print("Invalid Number of Command Line arguments")
        print("Use the given flags as :" )
        print("--u: used to displauy the usage ")
        print("--h: used to display the help")

    print(Border)
    print("-----------Thank you for using our script-----------")
    print("----------------Marvellous Infosystems--------------")
    print(Border)

if __name__=="__main__":
    main()
