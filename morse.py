from textwrap import wrap
import time
from playsound import playsound



def init():
    direction = raw_input("> ")
    if direction == "1":
        etom()
    elif direction == "2":
        mtoe()
    else:
        print "Type 1 or 2"
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

            else:
                print "Error:Unknown value"

            letter = ""

        else:
            letter += i

    print wrd





def etom():
    print "Use underscores instead of spaces"
    eng = raw_input("input> ")
    enletrs = wrap(eng, 1)

    binline = ""

    for i in enletrs:
        if i == "a":
            binline += "102"
            print i

        elif i == "b":
            binline += "2010101"
            print i

        elif i == "c":
            binline += "2010201"
            print i

        elif i == "d":
            binline += "20101"
            print i

        elif i == "e":
            binline += "1"
            print i

        elif i == "f":
            binline += "1010201"
            print i

        elif i == "g":
            binline += "20201"
            print i

        elif i == "h":
            binline += "1010101"
            print i

        elif i == "i":
            binline += "101"
            print i

        elif i == "j":
            binline += "1020202"
            print i

        elif i == "k":
            binline += "20102"
            print i

        elif i == "l":
            binline += "1020101"
            print i

        elif i == "m":
            binline += "202"
            print i

        elif i == "n":
            binline += "201"
            print i

        elif i == "o":
            binline += "20202"
            print i

        elif i == "p":
            binline += "1020201"
            print i

        elif i == "q":
            binline += "2020102"
            print i

        elif i == "r":
            binline += "10201"
            print i

        elif i == "s":
            binline += "10101"
            print i

        elif i == "t":
            binline += "2"
            print i

        elif i == "u":
            binline += "10102"
            print i

        elif i == "v":
            binline += "1010102"
            print i

        elif i == "w":
            binline += "10202"
            print i

        elif i == "x":
            binline += "2010102"
            print i

        elif i == "y":
            binline += "2010202"
            print i

        elif i == "z":
            binline += "2020101"
            print i

        elif i == "_":
            binline += "0"

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



print "Morse Code Translator"
print "coded by Aaron Harnish"
print "----------------------"
print "Type \'1\' for english to morse"
print "Type \'2\' for morse to english"

init()
