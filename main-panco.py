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


def hc(c, S, M):
    count0 = 0
    count1 = 0
    for read in S:
        if read[c] == '0':
            count0 += 1
        elif read[c] == '1':
            count1 += 1
    if count0 > count1:
        return '0'
    elif count1 > count0:
        return '1'
    else:
        return '-'
            
                
def h(S, M, genome_length):
    consensus = [hc(c, S, M) for c in range(genome_length)]
    return consensus

def D(S, T):
    to_return = 0
    for i in range(len(S)):
        if (S[i] == '0' and T[i] == '0') or (S[i] == '1' and T[i] == '1'):
            to_return += 1
        elif (S[i] == '0' and T[i] == '1') or (S[i] == '1' and T[i] == '0'):
            to_return += -1
        else:
            to_return += 0
    return to_return

if __name__ == "__main__":
    with open(sys.argv[1]) as infile:
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


    s1 = set()
    s2 = set()

    s1.add(reads[0])

    for read in reads[1:]:
        if D(read, h(s1, reads, genome_length)) >= D(read, h(s2, reads, genome_length)):
            s1.add(read)
        else:
            s2.add(read)

 #   print(s1)
#
  #  print()
 #   print(s2)
        
    
    # print(''.join(chr1.contents))
    # print(''.join(chr2.contents))

    print(''.join(h(s1, reads, genome_length)))
#    print()
    print(''.join(h(s2, reads, genome_length)))
    
