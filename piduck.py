#!/bin/python3
# import sys
import argparse
from importlib import import_module
from time import sleep

key_layout = "us"
default_delay = 10
string_delay = 10

piparser = argparse.ArgumentParser()
piparser.add_argument("-i", "--input", help="File input")
piparser.add_argument(
    "-l", "--keyboardlayoutcode", help="Language codes specified by ISO639-1:2002"
)
piparser.add_argument("-d", "--defaultdelay", help="The default delay of execution")
piparser.add_argument(
    "-s", "--defaultchardelay", help="The default char delay of execution"
)
piargs = piparser.parse_args()
if piargs.keyboardlayoutcode is not None:
    key_layout = piargs.keyboardlayoutcode
if piargs.defaultdelay is not None:
    default_delay = piargs.defaultdelay
if piargs.defaultchardelay is not None:
    string_delay = piargs.defaultchardelay
try:
    keymap = import_module("pd_key_maps.keymap_" + key_layout)
except ModuleNotFoundError:
    exit(3)


def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


def string(string):
    for char in string:
        pharse(char, [], True)
        sleep(string_delay / 100)


def pharse(line, known, deltrue):
    global default_delay
    global string_delay
    if line != " ":
        command = line.split()
    else:
        command = [" "]
    if not deltrue:
        if command[0] == "DELAY":
            sleep(int(command[1]) / 100)
            return
        elif command[0] == "REM":
            return
        elif command[0] == "REPEAT":
            return  # todo
        else:
            sleep(default_delay / 100)
    if command[0] == "STRING":
        string(" ".join(command[1:]))
        return
    elif command[0] == "DEFAULTCHARDELAY":
        string_delay = int(command[1])
        return
    elif command[0] == "DEFAULTDELAY":
        default_delay = int(command[1])
        return
    elif command[0] in keymap.aliasmap:
        pharse(keymap.aliasmap[command[0]] + " " + " ".join(command[1:]), known, True)
        return
    elif command[0] in keymap.commap:
        known.append(keymap.commap[command[0]])
        pharse(" ".join(command[1:]), known, True)
        return
    elif command[0] in keymap.c1map:
        known.append(keymap.c1map[command[0]])
        out(known)
        return
    elif command[0] in keymap.c2map:
        pharse(keymap.c2map[command[0]], known, True)
        return
    else:
        exit(2)


def out(ccl):
    # ccl_part=list(divide_chunks(ccl, n))
    i = 2
    if len(ccl) == 1:
        rep = (chr(0) * 2) + chr(ccl[0])
        e = 3
    else:
        rep = ""
        for e in range(len(ccl) - 1):
            rep = rep + chr(ccl[e])
        e = e + 2
        rep = rep + chr(0) + chr(ccl[e - 1])
    rep = rep + (chr(0) * (8 - e))
    with open("/dev/hidg0", "rb+") as fd:
        fd.write(rep.encode())
        fd.write((chr(0) * 8).encode())


# argparse fix
def main():
    if piargs.input is not None:
        file1 = open(piargs.input, "r")
        while True:
            line = file1.readline()
            if not line:
                break
            pharse(line.strip(), [], False)
        file1.close()
    else:
        while True:
            line = input()
            if not line:
                break
            pharse(line.strip(), [], False)


main()
exit(0)
