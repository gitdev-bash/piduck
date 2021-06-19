#!/usr/bin/env python3
import argparse
from importlib import import_module
from time import sleep
import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def string(string):
    for char in string:
        pharse_p2(char, [[], []], True)
        sleep(string_delay / 100)


def pharse_p1(line):
    global default_delay
    global string_delay
    global last_line
    if line == "":
        return
    elif line == " ":
        command = [" "]
    else:
        command = line.split()
    if command[0] == "DELAY":
        sleep(int(command[1]) / 100)
        return
    elif command[0] == "REM":
        return
    elif command[0] == "REPEAT":
        try:
            for i in range(int(command[1])):
                pharse_p2(last_line.strip(), [[], []], False)
        except RecursionError:
            eprint("RecursionError!")
            exit(4)
        return
    elif command[0] == "DEFAULTCHARDELAY":
        string_delay = int(command[1])
        return
    elif command[0] == "DEFAULTDELAY":
        default_delay = int(command[1])
        return
    elif command[0] == "STRING":
        sleep(default_delay / 100)  # DEFAULT_DELAY
        string(line[len(command[0] + " ") :])
        last_line = line
        return
    else:
        pharse_p2(line, [[], []], False)
        last_line = line
        return


def pharse_p2(line, known, deltrue):
    if line == "":
        return
    elif line == " ":
        command = [" "]
    else:
        command = line.split()
    if command[0] in keymap.commap:
        known[0].append(keymap.commap[command[0]])
        if len(command) > 1:
            pharse_p2(" ".join(command[1:]), known, True)
        else:
            out(known)
        return
    elif command[0] in keymap.c1map:
        known[1].append(keymap.c1map[command[0]])
        if len(command) > 1:
            pharse_p2(" ".join(command[1:]), known, True)
        else:
            out(known)
        return
    elif command[0] in keymap.c2map:
        pharse_p2(keymap.c2map[command[0]] + " " + " ".join(command[1:]), known, True)
        return
    elif command[0] in aliasmap:
        pharse_p2(aliasmap[command[0]] + " " + " ".join(command[1:]), known, True)
        return
    else:
        eprint('Could not find "' + command[0] + '"')
        exit(2)


def out(ccl):
    rep = ""
    if len(ccl[0]) > 0:
        for e in ccl[0]:
            rep = rep + chr(e)
    else:
        rep = rep + chr(0)
    rep = rep + chr(0)
    for e in ccl[1]:
        rep = rep + chr(e)
    rep = rep + chr(0) * (8 - len(rep))
    with open("/dev/hidg0", "rb+") as fd:
        fd.write(rep.encode())
        fd.write((chr(0) * 8).encode())


def main():
    global last_line
    if piargs.input is not None:
        file1 = open(piargs.input, "r")
        while True:
            line = file1.readline()
            if not line:
                break
            parse_p1(line)
        file1.close()
    else:
        while True:
            try:
                line = input()
            except EOFError:
                break
            if not line:
                break
            pharse_p1(line)


if __name__ == "__main__":
    last_line = ""
    key_layout = "us"
    default_delay = 10
    string_delay = 1

    aliasmap = {
        "CTRL": "LCTRL",
        "SHIFT": "LSHIFT",
        "ALT": "LALT",
        "META": "LMETA",
        "CONTROL": "CTRL",
        "GUI": "META",
        "ESCAPE": "ESC",
        "RIGHTARROW": "RIGHT",
        "LEFTARROW": "LEFT",
        "DOWNARROW": "DOWN",
        "UPARROW": "UP",
        "CTRL-ALT": "CTRL ALT",
        "CTRL-SHIFT": "CTRL SHIFT",
        "DEFAULT_DELAY": "DEFAULTDELAY",
        " ": "SPACE",
        "BREAK": "PAUSE",
    }

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
        eprint('Keymap "' + key_layout + '" could not be found')
        exit(3)
    try:
        main()
    except KeyboardInterrupt:
        pass
    exit(0)
