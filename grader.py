#!/usr/bin/env python3

import sys

with open(sys.argv[1]) as keyfile:
    key_chrs1 = [line.strip() for line in keyfile]
    key_chrs2 = list(reversed(key_chrs1))

with open(sys.argv[2]) as testfile:
    test_chrs = [line.strip() for line in testfile]

if len(key_chrs1) != len(test_chrs):
    print("files don't have same number of lines")
    sys.exit()

no_attempts = 0
wrongs = 0
rights = 0

for line_index in range(len(key_chrs1)):
    for char_index in range(len(key_chrs1[line_index])):
        if test_chrs[line_index][char_index] == '-':
            no_attempts += 1
            continue
        if key_chrs1[line_index][char_index] != test_chrs[line_index][char_index]:
            wrongs += 1
        else:
            rights +=  1

print("no_att\twrongs\trights")
print(no_attempts, wrongs, rights, sep='\t')

no_attempts = 0
wrongs = 0
rights = 0

for line_index in range(len(key_chrs2)):
    for char_index in range(len(key_chrs2[line_index])):
        if test_chrs[line_index][char_index] == '-':
            no_attempts += 1
            continue
        if key_chrs2[line_index][char_index] != test_chrs[line_index][char_index]:
            wrongs += 1
        else:
            rights +=  1

print(no_attempts, wrongs, rights, sep='\t')
