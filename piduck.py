#!/bin/python3
import sys
from importlib import import_module
from time import sleep

key_layout = "us"
try:
    import_module("pd_key_maps.keymap_" + key_layout)
except ModuleNotFoundError:
    exit(3)

default_delay = 10
string_delay = 10


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
    command = line.split()
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
    elif command[0] in aliasmap:
        pharse(aliasmap[command[0]] + " ".join(command[1:]), True)
        return
    elif command[0] in commap:
        known.append(commap[command[0]])
        pharse(" ".join(command[1:]), known, True)
        return
    elif command[0] in c1map:
        known.append(c1map[command[0]])
        out(known)
        return
    else:
        exit(2)


def out(ccl):
    # ccl_part=list(divide_chunks(ccl, n))
    rep = chr(0) * 2
    i = 2
    for e in ccl:
        i += 1
        rep = rep + chr(e)
    rep = rep + (chr(0) * (8 - i))
    with open("/dev/hidg0", "rb+") as fd:
        fd.write(rep.encode())
        fd.write((chr(0) * 8).encode())


def main():
    if len(sys.argv) >= 2:
        file1 = open(sys.argv[1], "r")
        while True:
            line = file1.readline()
            if not line:
                break
            pharse(line.strip(), [], False)
        file1.close()
    elif len(sys.argv) == 1:
        while True:
            line = input()
            if not line:
                break
            pharse(line.strip(), [], False)


main()
exit(0)
