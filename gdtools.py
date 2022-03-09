# GD TOOLS 1.0 by SA ST
loop = 0
from os import path


nooptionloop = 0
option_exist = path.exists("options.gdtools")
while nooptionloop == 0:
    if option_exist == False:
        print("Optionfile not found. Creating a new one.")
        optionfile = open("options.gdtools", "a")
        optionfile.write("False")
    else:
        optionfile = open("options.gdtools", "a")
        print("Optionfile found.")
        nooptionloop = 1
    readoption = open("options.gdtools", "r")
    request_option = readoption.readline() 
    if request_option == "False":
        requestloop = 0
        while requestloop == 0:
            requests = input("Do you have requests installed (y/n) (CASE SENSETIVE)\n")
            if requests == "n":
                print('Please install requests using "pip install requests"\n')
                exit()
            elif requests == "y":
                print("Saving Optionfile")
                optionwrite = open("options.gdtools", "w")
                optionwrite.write("True")
                requestloop = 1
            else:
                print("Error! Please try again.")
print("""  ____ ____  _____ ___   ___  _     ____
 / ___|  _ \|_   _/ _ \ / _ \| |   / ___|
| |  _| | |   | || | | | | | | |   \___ )
| |_| | |_|   | || |_| | |_| | |___ ___) |
 \____|____/  |_| \___/ \___/|_____|____/
 BY SA ST
""")
from requests import get
while loop == 0:
    command = input("> ")
    if command == "exit":
        print("Thanks for using GD TOOLS\n")
        exit()
    elif command == "download -s":
        song_download_id = input("Enter LevelID: ")
        song_download_gd = get('https://gdbrowser.com/api/level/' + song_download_id)
        song_download_songlink = song_download_gd.json()['songLink']
        song_download_mp3 = get(song_download_songlink, stream = True)
        with open(song_download_gd.json()['songName'] + ".mp3", "wb") as song_download_file:
            for song_download_chunk in song_download_mp3.iter_content(chunk_size = 16*1024):
                song_download_file.write(song_download_chunk) # thank you https://365datascience.com/tutorials/python-tutorials/python-requests-package/
                print("Song downloaded. Look for the .mp3 file")
    elif command == help:
    else:
        print("Error")