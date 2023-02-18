from sys import*

def fun(Parameter):

    #Logic of Script

def main():
    print("----Marvellous Infosystems by Piyush Khairmar----")
    print("Application name : "+argv[0])

    if(len(argv) != 3):
        print("This Script is designed for --------------")
        exit()

    if argv[1] == "-h":
        print("This Script is designed for-----------")
        exit()

    if argv[1] == "-u":
        print("Usage : Application_Name------------")
        exit()

    try:
        fun(argv[1])

    except Exception as E:
        print("Error : Invalid input"+E)

    if ((len(argv) < 1) or (len(argv) > 3)):
        print("Error : Invalid number of arguments")

if __name__ == "__main__":
    main()