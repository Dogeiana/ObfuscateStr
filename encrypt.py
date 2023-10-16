import random
import sys

char_to_number = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
    'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
    'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
    '1': 27, '2': 28, '3': 29, '4': 30, '5': 31, '6': 32, '7': 33, '8': 34, '9': 35, '0': 36,
    ' ': 37, '!': 38, '"': 39, '#': 40, '$': 41, '%': 42, '&': 43, "'": 44, '(': 45, ')': 46,
    '*': 47, '+': 48, ',': 49, '-': 50, '.': 51, '/': 52, ':': 53, ';': 54, '<': 55, '=': 56,
    '>': 57, '?': 58, '@': 59, '[': 60, '\\': 61, ']': 62, '^': 63, '_': 64, '`': 65, '{': 66,
    '|': 67, '}': 68, '~': 69
}
 
keys = [0xff, # use to skip 0 
        0xdeadbeef, 
        0xdeadc0de, 
        0xfeedface,
        0xB16B00B5
        ]
data_bytes = []

def main(edata): # encrypt the data
    key_rand = random.randint(1, len(keys))
    for char in edata:
        char_byte = char_to_number.get(char, 0) 
        for key in keys:
            key_index = len(data_bytes) % key_rand
            key_byte = (key >> (8 * key_index)) & 0xFF
            char_byte ^= key_byte
        data_bytes.append(char_byte)

    data = bytes(data_bytes)

    print(data)
    print(f"Keys: {key_rand}") # use this the decrypt

if len(sys.argv) != 2:
    print(f"Usage: python3 {sys.argv[0]} <string_data>")
    sys.exit(1)

string_data = sys.argv[1]
main(string_data)
