import time
from playsound import playsound

# Dictionary containing all accepted morse symbols and their english counterparts.
morseToEnglishDict = {"_": " ", ".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g",
                      "....": "h",
                      "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p",
                      "--.-": "q",
                      ".-.": "r", "...": "s", "-": "t", "..-": "u", "...-": "v", ".--": "w", "-..-": "x", "-.--": "y",
                      "--..": "z",
                      ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6", "--...": "7",
                      "---..": "8", "----.": "9", "-----": "0"}

# Calls functions of morse.py after user input
def init():
    direction = input("> ")
    if direction == "1":
        englishToMorse()
    elif direction == "2":
        morseToEnglish()
    elif direction == "q":
        exit()
    else:
        print("Type 1, 2, or q")
        init()

#Prints the english equivalent of inputted morse code
#Input ".../---/..." prints "sos"
def morseToEnglish():
    print("Type morse in this format:")
    print(".../---/.../_/.../---/... = sos sos")

    morseInput = input("> ")
    inputSliced = morseInput.split("/")

    print(inputSliced)

    output = ""
    for i in inputSliced:
        output += morseToEnglishDict[i]

    print(output)

    time.sleep(2)
    start()

# Prints the english input as morse code sound plays, then prints the morse code in same format as before
def englishToMorse():
    #Swaps keys and values of englishToMorseDict, could be more efficient to just include the dict.
    englishToMorseDict = {}
    for k, v in morseToEnglishDict.items():
        englishToMorseDict[v] = k

    englishInput = input("English input > ")

    morseReturn = ""

    for i in englishInput:
        morse = englishToMorseDict[i]
        print(i, end="")
        playMorseSound(morse)
        morseReturn += "/" + morse

    print(morseReturn)

    time.sleep(2)
    start()

#Helper function for englishToMorse(), plays the morse sound.
def playMorseSound(morse):
    for i in morse:
        # Plays short dit morse sound
        if i == ".":
            pass
            # playsound("beep10.mp3") lost old sound files
        elif i == ",":
            pass
            # playsound("beep30.mp3") lost old sound files
        elif i == "/":
            #Sleeps same length as a dit
            time.sleep(0.1)

#Called when morse.py is run and 2s after etom or mtoe functions are completed.
def start():
    print("----------------------")
    print("Type \'1\' for english to morse")
    print("Type \'2\' for morse to english")
    print("Type \'q\' to exit program")

    init()


start()
