#! /usr/bin/env python
##
import hashlib
import sys
import pickle

_differences = []

def save_differences(diff):
    with open('differences.txt', 'w') as file:
        pickle.dump(diff, file)

def load_differences():
    try:
        with open('differences.txt', 'r') as file:
            return pickle.load(file)
    except:
        return None

def calculate_hex(hexadecimal):
    word = []
    for single_hex in hexadecimal:
        first_hex = single_hex[0].zfill(4)
        second_hex = single_hex[1].zfill(4)

        first_hex = int(first_hex, 16)
        second_hex = int(second_hex, 16)

        if first_hex > second_hex:
            letter = first_hex - second_hex
            word.append(chr(letter))
        elif second_hex > first_hex:
            letter = second_hex - first_hex
            try:
                word.append(unichr(letter))
            except ValueError:
                pass

    return ''.join(word)

def remove_duplicate(string1, string2):
    unique1 = []
    unique2 = []
    for ch1, ch2 in zip(string1, string2):
        if ch1 != ch2:
            unique1.append(ch1)
            unique2.append(ch2)
    return (''.join(unique1), ''.join(unique2))

def find_differences():
    differences = []
    i = 0
    with open('original', 'r') as file:
        data = file.read()
        lines = data.split('\n')
        for line in lines:
            i += 1
            hash = str(i)

            for iters in range(512):
                hash = hashlib.sha512(hash).hexdigest()

            if hash not in line:
                differences.append(remove_duplicate(line.strip(), hash.strip()))
                save_differences(differences)

            sys.stdout.write('\r%d / %d completed' % (i, len(lines)))
            sys.stdout.flush()
    return differences


if __name__ == '__main__':
    _differences = load_differences()
    if _differences == None:
        _differences = find_differences()

    print('FLAG: %s' % calculate_hex(_differences))

