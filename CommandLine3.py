import sys

def main():
    print("Command Line Arguments are: ")
    for i in range(len(sys.argv)):
        print(sys.argv[i])      
    print(len(sys.argv))
    
if __name__=="__main__":
    main()
