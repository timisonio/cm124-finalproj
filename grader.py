#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as keyfile:
    key_chrs = [line.strip() for line in keyfile]

with open(sys.argv[2]) as testfile:
    test_chrs = [line.strip() for line in testfile]

if len(key_chrs) != len(test_chrs):
    print("files don't have same number of lines")
    sys.exit()

no_attempts = 0
wrongs = 0

for line_index in range(len(key_chrs)):
    for char_index in range(len(key_chrs[line_index])):
        if test_chrs[line_index][char_index] == '-':
            no_attempts += 1
            continue
        if key_chrs[line_index][char_index] != test_chrs[line_index][char_index]:
            wrongs += 1

print(no_attempts, wrongs)

