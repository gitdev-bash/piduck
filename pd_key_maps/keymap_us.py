#!/bin/python3
commap = {
    "LCTRL": 1,
    "LSHIFT": 2,
    "LALT": 4,
    "LMETA": 8,
    "RCTRL": 16,
    "RSHIFT": 32,
    "RALT": 64,
    "RMETA": 128,
}
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
    "CTRL": "LCTRL",
    "SHIFT": "LSHIFT",
    "ALT": "LALT",
    "META": "LMETA",
    "CONTROL": "CTRL",
    "CTRL-ALT": "CTRL ALT",
    "CTRL-SHIFT": "CTRL SHIFT",
    "DEFAULT_DELAY": "DEFAULTDELAY",
    " ": "SPACE",
}