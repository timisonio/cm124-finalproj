#!/usr/bin/env python3

''' 
Timothy Isonio
704300058
Hum Gen CM124 Section 1
May/June 2016

Haplotype Assembly Final Project
'''

import sys
from collections import defaultdict

class Read:
    def __init__(self, read, pos):
        self.read = read
        self.pos = pos

class Chromosome:
    def __init__(self, length):
        self.contents = ['-' for i in range(length)]

if __name__ == "__main__":
    with open(sys.argv[1]) as infile:
        # reads = []
        # for line in infile:
        #     genome_length = len(line.strip())
        #     read_contents = []
        #     read_offset = 0
        #     read_started = False
        #     for char in line:
        #         if char == '0' or char == '1':
        #             read_contents.append(char)
        #             read_started = True
        #         else:
        #             if read_started is False:
        #                 read_offset += 1
        #                 read_contents = ''.join(read_contents)
        #     reads.append(Read(read_contents, read_offset))

        reads = [line.strip() for line in infile]

    genome_length = len(reads[0])

    chr1 = Chromosome(genome_length)
    chr2 = Chromosome(genome_length)


    
    for pos in range(genome_length):
        versions = defaultdict(int)
        for read in reads:
            if read[pos] != '-':
                versions[read[pos]] += 1
                
        # handle trival cases, where all reads that cover a position agree
        if len(versions) == 1:
            chr1.contents[pos] = list(versions.keys())[0]  # take the first member of the keys list... the only member
            chr2.contents[pos] = list(versions.keys())[0]

        
    print(''.join(chr1.contents))
    print(''.join(chr2.contents))
    
