from textwrap import wrap
import time
from playsound import playsound



def init():
    direction = raw_input("> ")
    if direction == "1":
        etom()
    elif direction == "2":
        mtoe()
    elif direction == "q":
        exit()
    else:
        print "Type 1, 2, or q"
        init()


def dot():
    print "DOT"
    playsound("beep10.mp3")

def dash():
    print "DASH"
    playsound("beep30.mp3")


def mtoe():
    print "Type morse in this format:"
    print ".../---/.../_/.../---/.../ = sos sos"
    print "You must put a / after every letter or space"

    inp = raw_input("> ")
    inpslc = wrap(inp, 1)

    letter = ""
    wrd = ""

    for i in inpslc:
        if i == "/":
            if letter == "_":
                wrd += " "

            elif letter == ".-":
                wrd += "a"

            elif letter == "-...":
                wrd += "b"

            elif letter == "-.-.":
                wrd += "c"

            elif letter == "-..":
                wrd += "d"

            elif letter == ".":
                wrd += "e"

            elif letter == "..-.":
                wrd += "f"

            elif letter == "--.":
                 wrd += "g"

            elif letter == "....":
                 wrd += "h"

            elif letter == "..":
                wrd += "i"

            elif letter == ".---":
                 wrd += "j"

            elif letter == "-.-":
                 wrd += "k"

            elif letter == ".-..":
                 wrd += "l"

            elif letter == "--":
                 wrd += "m"

            elif letter == "-.":
                 wrd += "n"

            elif letter == "---":
                 wrd += "o"

            elif letter == ".--.":
                 wrd += "p"

            elif letter == "--.-":
                 wrd += "q"

            elif letter == ".-.":
                 wrd += "r"

            elif letter == "...":
                 wrd += "s"

            elif letter == "-":
                 wrd += "t"

            elif letter == "..-":
                 wrd += "u"

            elif letter == "...-":
                 wrd += "v"

            elif letter == ".--":
                 wrd += "w"

            elif letter == "-..-":
                 wrd += "x"

            elif letter == "-.--":
                 wrd += "y"

            elif letter == "--..":
                 wrd += "z"

            elif letter == ".----":
                wrd += "1"

            elif letter == "..---":
                wrd += "2"

            elif letter == "...--":
                wrd += "3"

            elif letter == "....-":
                wrd += "4"

            elif letter == ".....":
                wrd += "5"

            elif letter == "-....":
                wrd += "6"

            elif letter == "--...":
                wrd += "7"

            elif letter == "---..":
                wrd += "8"

            elif letter == "----.":
                wrd += "9"

            elif letter == "-----":
                wrd += "0"

            else:
                print "Error:Unknown value"

            letter = ""

        else:
            letter += i

    print wrd

    time.sleep(2)
    start()




def etom():
    print "Use underscores instead of spaces"
    eng = raw_input("input> ")
    enletrs = wrap(eng, 1)

    binline = ""

    for i in enletrs:
        if i == "a":
            binline += "102"


        elif i == "b":
            binline += "2010101"


        elif i == "c":
            binline += "2010201"


        elif i == "d":
            binline += "20101"


        elif i == "e":
            binline += "1"


        elif i == "f":
            binline += "1010201"


        elif i == "g":
            binline += "20201"


        elif i == "h":
            binline += "1010101"


        elif i == "i":
            binline += "101"


        elif i == "j":
            binline += "1020202"


        elif i == "k":
            binline += "20102"


        elif i == "l":
            binline += "1020101"


        elif i == "m":
            binline += "202"


        elif i == "n":
            binline += "201"


        elif i == "o":
            binline += "20202"


        elif i == "p":
            binline += "1020201"


        elif i == "q":
            binline += "2020102"


        elif i == "r":
            binline += "10201"


        elif i == "s":
            binline += "10101"


        elif i == "t":
            binline += "2"


        elif i == "u":
            binline += "10102"


        elif i == "v":
            binline += "1010102"


        elif i == "w":
            binline += "10202"


        elif i == "x":
            binline += "2010102"


        elif i == "y":
            binline += "2010202"


        elif i == "z":
            binline += "2020101"


        elif i == "_":
            binline += "0"


        elif i == "1":
            binline += "102020202"


        elif i == "2":
            binline += "101020202"


        elif i == "3":
            binline += "101010202"


        elif i == "4":
            binline += "101010102"


        elif i == "5":
            binline += "101010101"


        elif i == "6":
            binline += "201010101"


        elif i == "7":
            binline += "202010101"


        elif i == "8":
            binline += "202020101"


        elif i == "9":
            binline += "202020201"


        elif i == "0":
            binline += "202020202"


        else:
            print "error: unrecognized input"

        binline += "000"

    for i in binline:
        if i == "2":
            dash()
        elif i == "1":
            dot()
        elif i == "0":
            time.sleep(0.1)
        else:
            print "Error: not 2 or 1 or 0"

    print binline

    time.sleep(2)
    start()



def start():
    print "Morse Code Translator"
    print "coded by Aaron Harnish"
    print "----------------------"
    print "Type \'1\' for english to morse"
    print "Type \'2\' for morse to english"
    print "Type \'q\' to exit program"

    init()

start()
