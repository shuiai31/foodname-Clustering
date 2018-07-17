#!/usr/bin/env python 
# find an LCS (Longest Common Subsequence). 
# *public domain* 

def find_lcs_len(s1, s2):
    m = [ [ 0 for x in s2 ] for y in s1 ] # creates a matrix with all elements set to 0
    for p1 in range(len(s1)):
        for p2 in range(len(s2)):
            if s1[p1] == s2[p2]:
                if p1 == 0 or p2 == 0:
                    m[p1][p2] = 1
                else:
                    m[p1][p2] = m[p1-1][p2-1]+1
            elif m[p1-1][p2] < m[p1][p2-1]:
                m[p1][p2] = m[p1][p2-1]
            else:                             # m[p1][p2-1] < m[p1-1][p2]
                m[p1][p2] = m[p1-1][p2]
    return m[-1][-1]

def find_lcs(s1, s2): # matrix as high as the first word and as wide as the second. it's filled with 0 in the beginning, then as the program enters the for loop values inisde changes.
    # length table: every element is set to zero.
    m = [ [ 0 for x in s2 ] for y in s1 ]
    # direction table: 1st bit for p1, 2nd bit for p2.
    d = [ [ None for x in s2 ] for y in s1 ]
    # we don't have to care about the boundery check.
    # a negative index always gives an intact zero.
    for p1 in range(len(s1)):
        for p2 in range(len(s2)):
            if s1[p1] == s2[p2]:
                if p1 == 0 or p2 == 0: # it only sets to 1 if the elemnts is at the top or left end, otherswise it sets the value to that of it's upper left neighbor +1
                    m[p1][p2] = 1  # means that an element in the matrix m changes to 1 at position p1, p2
                else:
                    m[p1][p2] = m[p1-1][p2-1]+1
                d[p1][p2] = 3                   # 11: decr. p1 and p2
            elif m[p1-1][p2] < m[p1][p2-1]:
                m[p1][p2] = m[p1][p2-1]
                d[p1][p2] = 2                   # 10: decr. p2 only
            else:                             # m[p1][p2-1] < m[p1-1][p2]
                m[p1][p2] = m[p1-1][p2]
                d[p1][p2] = 1                   # 01: decr. p1 only
    (p1, p2) = (len(s1)-1, len(s2)-1)
    # now we traverse the table in reverse order.
    s = []
    while 1:
        print p1,p2
        c = d[p1][p2]
        if c == 3: s.append(s1[p1])
        if not ((p1 or p2) and m[p1][p2]): break
        if c & 2: p2 -= 1
        if c & 1: p1 -= 1
    s.reverse()
    return ''.join(s)



