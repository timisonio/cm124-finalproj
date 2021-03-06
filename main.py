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
    def __init__(self, length, contents=None):
        self.contents = ['-' for i in range(length)]
        if contents != None:
            if length == len(contents):
                self.contents = contents
            else:
                print("length error")
                sys.exit()

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
    
    reads_only = [ ''.join([char for char in read if char != '-']) for read in reads]

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

    # get rid of duplicate reads
    duplicate_read_indices = set()
    for read_index in range(len(reads)):
        for read_index_2 in range(read_index + 1, len(reads)):
            if(read_index_2 > read_index + 20):
                # don't look too far
                break
            if reads[read_index] == reads[read_index_2]:
                duplicate_read_indices.add(read_index_2)
    while len(duplicate_read_indices) > 0:
        duplicate_read_indices.pop()

    chr1_updated = ['-' for i in range(genome_length)]
    chr2_updated = ['-' for i in range(genome_length)]
    for read in reads:
        entire_read_maps = True
        for char_index in range(len(read)):
            if chr1.contents[char_index] != '-' and read[char_index] != '-' and chr1.contents[char_index] != read[char_index]:
                entire_read_maps = False
                break
        if entire_read_maps is True:
            for char_index in range(len(read)):
                if chr1.contents[char_index] == '-':
                    if chr1_updated[char_index] == '-':
                        chr1_updated[char_index] = read[char_index]
                    elif chr1_updated[char_index] != read[char_index]:
                        chr2_updated[char_index] = read[char_index]

    #print(chr1_updated)

    for char_index in range(len(chr1_updated)):
        if chr1_updated[char_index] not in "-?":
            chr1.contents[char_index] = chr1_updated[char_index]
                        
#        print(''.join(chr1.contents))
            
        
    
    print(''.join(chr1.contents))
    print(''.join(chr2.contents))
    
