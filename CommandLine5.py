#python CommandLine5.py 11 10

import sys

def main():
    if (len(sys.argv)<3 or len(sys.argv)>3):
        print("Invalid number of arguments")
    else:
        No1=int(sys.argv[1])
        No2=int(sys.argv[2])
        print(No1+No2) 

if __name__=="__main__":
    main()

    import sys

def main():
    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]

    fobj1 = open(FileName1,"r")
    fobj2 = open(FileName2,"r")

    data1 = fobj1.read()
    data2 = fobj2.read()

    fobj1.close()
    fobj2.close()

    if data1==data2:
        print("Success!!!!!")
    else:
        print("Failure :/")


if __name__=="__main__":
    main()
