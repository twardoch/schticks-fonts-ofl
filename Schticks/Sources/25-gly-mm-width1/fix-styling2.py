#!/usr/bin/env python

import os
import fnmatch
from fontTools.ttLib import TTFont
import sys

fol = sys.argv[1]
outfol = sys.argv[2]

if not os.path.exists(outfol): 
    os.makedirs(outfol)

def getFiles(): 
    l = []
    for fn in os.listdir(fol):
        if fnmatch.fnmatch(fn, '*.?tf'):
            l.append(fn)
    return l

def fixStyle(fn):
    fp = os.path.join(fol, fn)
    outfp = os.path.join(outfol, fn)
    f = TTFont(fp)
    typf = f['name'].getName(16, 3, 1, 0x409)
    macf = f['name'].getName(1, 1, 0, 0)
    macf.string = typf.string.decode('utf-16-be').encode('mac-roman')
    typs = f['name'].getName(17, 3, 1, 0x409)
    macs = f['name'].getName(2, 1, 0, 0)
    macs.string = typs.string.decode('utf-16-be').encode('mac-roman')
    f.save(outfp)
    return outfp, macf.string, macs.string

def main(): 
    for fn in getFiles():
        print(fixStyle(fn))

main()
