#!/usr/bin/env python

import os
import fnmatch
from fontTools.ttLib import TTFont

uprfol = 'otfu'
itafol = 'otfi'
outfol = 'otf'

def getUprs(): 
    l = []
    for fn in os.listdir(uprfol):
        if fnmatch.fnmatch(fn, '*.otf'):
            l.append(os.path.splitext(fn)[0])
    return l

def getUprItas(): 
    l = []
    for upr in getUprs(): 
        l.append((upr, "{}It".format(upr)))
    return l

def fixUprIta(upr, ita):
    inpupr = os.path.join(uprfol, "{}.otf".format(upr))
    outpupr = os.path.join(outfol, "{}.otf".format(upr))
    inpita = os.path.join(itafol, "{}.otf".format(ita))
    outpita = os.path.join(outfol, "{}.otf".format(ita))
    fupr = TTFont(inpupr)
    fita = TTFont(inpita)
    nita = fita['name'].getName(1, 3, 1, 0x409)
    nupr = fupr['name'].getName(1, 3, 1, 0x409)
    nita.string = nupr.string
    nita = fita['name'].getName(1, 1, 0, 0)
    nupr = fupr['name'].getName(1, 1, 0, 0)
    nita.string = nupr.string
    fupr.save(outpupr)
    fita.save(outpita)
    return (inpupr, outpupr, inpita, outpita)

def main(): 
    for upr, ita in getUprItas():
        print(fixUprIta(upr, ita))

main()