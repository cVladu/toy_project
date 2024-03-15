# -*- coding: utf-8 -*-
SYMBOLS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def to_roman(number: int):
    numerals = []
    while number >= 1:
        for symbol, value in SYMBOLS.items():
            if value <= number:
                numerals.append(symbol)
                number -= value
                break
    return "".join(numerals)
