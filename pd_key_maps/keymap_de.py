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
    "z": 28,
    "y": 29,
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
    "ß": 45,
    "´": 46,
    "ü": 47,
    "+": 48,
    "#": 49,
    #    "#": 50,  # Non us only
    "ö": 51,
    "ä": 52,
    "^": 53,
    ",": 54,
    ".": 55,
    "-": 56,
    "CAPSLOCK": 57,
    "F1": 58,
    "F2": 59,
    "F3": 60,
    "F4": 61,
    "F5": 62,
    "F6": 63,
    "F7": 64,
    "F8": 65,
    "F9": 66,
    "F10": 67,
    "F11": 68,
    "F12": 69,
    "PRINT": 70,
    "SCROLLLOCK": 71,
    "PAUSE": 72,
    "INSERT": 73,
    "HOME": 74,
    "PAGEUP": 75,
    "DELETE": 76,
    "END": 77,
    "PAGEDOWN": 78,
    "RIGHT": 79,
    "LEFT": 80,
    "DOWN": 81,
    "UP": 82,
    "NUMLOCK": 83,
    # kp-divide:"54",
    # kp-multiply:"55",
    # kp-minus:"56",
    # kp-plus:"57",
    # kp-return:"58",
    # kp-1:"59",
    # kp-2:"5a",
    # kp-3:"5b",
    # kp-4:"5c",
    # kp-5:"5d",
    # kp-6:"5e",
    # kp-7:"5f",
    # kp-8:"60",
    # kp-9:"61",
    # kp-0:"62",
    # kp-period:"63",
    # application:"65",
    # power:"66",
    # kp-equal:"67",
    "F13": 104,
    "F14": 105,
    "F15": 106,
    "F16": 107,
    "F17": 108,
    "F18": 109,
    "F19": 110,
    "F20": 111,
    "F21": 112,
    "F22": 113,
    "F23": 114,
    "F24": 115,
    # execute:116,
    # help:117,
    # menu:118,
    # select:119,
    # cancel:120,
    # redo:121,
    # undo:122,
    # cut:123,
    # copy:124,
    # paste:125,
    # find:126,
    # mute:127,
    # volume-up:128,
    # volume-down:129,
}
c2map = {
    "°": "SHIFT ^",
    "!": "SHIFT 1",
    '"': "SHIFT 2",
    "§": "SHIFT 3",
    "$": "SHIFT 4",
    "%": "SHIFT 5",
    "&": "SHIFT 6",
    "/": "SHIFT 7",
    "(": "SHIFT 8",
    ")": "SHIFT 9",
    "=": "SHIFT 0",
    "?": "SHIFT ß",
    "`": "SHIFT ´",
    "<": "SHIFT ,",
    ">": "SHIFT .",
    #    "?": "SHIFT /",
    #    '"': "SHIFT '",
    ":": "SHIFT ;",
    "{": "SHIFT [",
    "}": "SHIFT ]",
    "|": "SHIFT \\",
}
for i in range(65, 91):
    c2map[chr(i)] = "SHIFT " + chr(i).lower()
