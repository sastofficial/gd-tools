# GD TOOLS 1.0 by SA ST
loop = 0
from os import path



option_exist = path.exists("options.gdtools")
if option_exist == False:
    print("Optionfile not found. Creating a new one.")
    optionfile = open("options.gdtools", "a")
    optionfile.write("False")
else:
    optionfile = open("options.gdtools", "a")
    print("Optionfile found.")
readoption = open("options.gdtools", "r")
request_option = readoption.readline() 
if request_option == "False":
    requestloop = 0
    while requestloop < 1:
        requests = input("Do you have requests installed (y/n) (CASE SENSETIVE)\n")
        if requests == "n":
            print('Please install requests using "pip install requests"\n')
            exit()
        elif requests == "y" or "Y":
            print("Saving Optionfile")
            optionwrite = open("options.gdtools", "w")
            optionwrite.write("True")
            requestloop = requestloop + 1
        else:
            print("Error! Please try again.")
print("test")

