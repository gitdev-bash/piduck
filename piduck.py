#!/bin/python3
import sys
from time import sleep

commap = {}
c1map = {
    "a": 4,
    "b": 5,
    "c": 6,
    "d": 7,
    "e": 8,
    "f": 9,
    "g": 10,
    "h": 11,
    "i": 12,
    "j": 13,
    "k": 14,
    "l": 15,
    "m": 16,
    "n": 17,
    "o": 18,
    "p": 19,
    "q": 20,
    "r": 21,
    "s": 22,
    "t": 23,
    "u": 24,
    "v": 25,
    "w": 26,
    "x": 27,
    "y": 28,
    "z": 29,
    "1": 30,
    "2": 31,
    "3": 32,
    "4": 33,
    "5": 34,
    "6": 35,
    "7": 36,
    "8": 37,
    "9": 38,
    "0": 39,
    "RETURN": 40,
    "ESC": 41,
    "BACKSPACE": 42,
    "TAB": 43,
    "SPACE": 44,
}
c2map = {}
for i in range(65, 91):
    c2map[chr(i)] = "SHIFT " + chr(i).lower()
aliasmap = {
    "CTRL-ALT": "CTRL ALT",
    "CTRL-SHIFT": "CTRL SHIFT",
    "DEFAULT_DELAY": "DEFAULTDELAY",
}
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
