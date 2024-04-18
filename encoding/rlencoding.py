# From: https://hypothesis.readthedocs.io/en/latest/quickstart.html
# (C) 2013-2024, David R. MacIver. Available under Mozilla Public License v 2.0
# https://github.com/HypothesisWorks/hypothesis/blob/master/LICENSE.txt
#
# Originally adapted from: https://rosettacode.org/wiki/Run-length_encoding
# Under GNU Free Document License 1.3
# https://www.gnu.org/licenses/fdl-1.3.en.html

def encode(input_string):
    count = 1
    prev = ""
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev, count)
                lst.append(entry)
            count = 1
            prev = character
        else:
            count += 1
    entry = (character, count)
    lst.append(entry)
    return lst


def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q
