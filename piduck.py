#!/bin/python3
# import sys
import argparse
from importlib import import_module
from time import sleep

key_layout = "us"
default_delay = 10
string_delay = 1

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
    if command[0] == "DELAY":
        sleep(int(command[1]) / 100)
        return
    elif command[0] == "REM":
        return
    elif command[0] == "REPEAT":
        return  # todo
    elif command[0] == "DEFAULTCHARDELAY":
        string_delay = int(command[1])
        return
    elif command[0] == "DEFAULTDELAY":
        default_delay = int(command[1])
        return
    else:
        if not deltrue:
            sleep(default_delay / 100)
    if command[0] == "STRING":
        string(line[len("STRING ") :])
        return
    elif command[0] in keymap.commap:
        known[0].append(keymap.commap[command[0]])
        pharse(" ".join(command[1:]), known, True)
        return
    elif command[0] in keymap.c1map:
        known[1].append(keymap.c1map[command[0]])
        out(known)
        return
    elif command[0] in keymap.c2map:
        pharse(keymap.c2map[command[0]], known, True)
        return
    elif command[0] in keymap.aliasmap:
        pharse(keymap.aliasmap[command[0]] + " " + " ".join(command[1:]), known, True)
        return
    else:
        exit(2)


def out(ccl):
    rep = ""
    if len(ccl[0]) > 0:
        for e in ccl[0]:
            rep = rep + chr(ccl[e])
    else:
        rep = rep + chr(0)
    rep = rep + chr(0)
    for e in ccl[1]:
        rep = rep + chr(ccl[e])
    rep = rep + chr(0) * (8 - len(rep))
    with open("/dev/hidg0", "rb+") as fd:
        fd.write(rep.encode())
        fd.write((chr(0) * 8).encode())


def main():
    if piargs.input is not None:
        file1 = open(piargs.input, "r")
        while True:
            line = file1.readline()
            if not line:
                break
            pharse(line.strip(), [[], []], False)
        file1.close()
    else:
        while True:
            line = input()
            if not line:
                break
            pharse(line.strip(), [[], []], False)


main()
exit(0)
