# GD TOOLS 1.0 by SA ST
loop = 0
from os import path
from urllib import request


option_exist = path.exists("options.gdtools")
if option_exist == False:
    print("Optionfile not found. Creating a new one.")
    optionfile = open("options.gdtools", "w")
    optionfile.write("False")
else:
    optionfile = open("options.gdtools", "w")
    print("Optionfile found.")
if optionfile.readline == "False":
    requestloop = 0
    while requestloop < 1:
        requests = input("Do you have requests installed (Y/N)\n")
        if requests == "n" or "N":
            print('Please install requests using "pip install requests"\n')
            exit()
        elif requests == "y" or "Y":
            print("Saving Optionfile")
            optionfile.write("True")
            requestloop = requestloop + 1
        else:
            print("Error! Please try again.")
print("test")