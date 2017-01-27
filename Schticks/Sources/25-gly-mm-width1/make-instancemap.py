#!/usr/bin/env python
# This script generates a text file
# the contents of which can be copied into the clipboard
# then pasted into the left pane of Glyphs 
# Font Info / Instances tab

def line(s, l): 
    s += l + "\n"
    return s

custs = {
    0: "", 
}

wghts = {
    60: ["100 Th", "Thin"], 
    66: ["200 ExLt", "ExtraLight"], 
    73: ["300 Lt", "Light"], 
    80: ["400 Rg", ""], 
    89: ["500 Md", "Medium"], 
    100: ["600 SmBd", "SemiBold"], 
    112: ["700 Bd", "Bold"], 
    125: ["800 ExBd", "ExtraBold"], 
    140: ["900 Blk", "Black"],
}

wdths = { 
    90: ["1 UlCd", "Ultra Condensed"], 
    92: ["2 ExCd", "Extra Condensed"], 
    95: ["3 Cd", "Condensed"], 
    97: ["4 SmCd", "SemiCondensed"], 
    100: ["5 No", ""], 
    102: ["6 SmWd", "Semi Expanded"], 
    105: ["7 Wd", "Expanded"], 
    107: ["8 ExWd", "Extra Expanded"], 
    110: ["9 UlWd", "Extra Expanded"], 
}
italics = { 
    0: ["", "SchticksText-MM"], 
    1: [" It", "SchticksText-MMI"], 
} 

italic = italics[1] # set 0 for upright, 1 for italic, then run

s = ''
s = line(s, '(')
for cust in sorted(custs.keys()): 
    for wdth in sorted(wdths.keys()): 
        for wght in sorted(wghts.keys()): 
            s = line(s, '        {')
#            s = line(s, '        customParameters =         (')
#            s = line(s, '                        {')
#            s = line(s, '                name = "Rename Glyphs";')
#            s = line(s, '                value =                 (')
#            s = line(s, '                    "six.alt=six,nine.alt=nine,g.alt=g,R.alt=R"')
#            s = line(s, '                );')
#            s = line(s, '            }')
#            s = line(s, '        );')
            s = line(s, '        interpolationCustom = %s;' % (cust))
            s = line(s, '        interpolationWeight = %s;' % (wght))
            s = line(s, '        interpolationWidth = %s;' % (wdth))
            s = line(s, '        name = "%s%s %s%s";' % (custs[cust], wdths[wdth][0], wghts[wght][0], italic[0]))
            if wghts[wght][1] != "": 
                s = line(s, '        weightClass = %s;' % (wghts[wght][1]))
            if wdths[wdth][1] != "": 
                s = line(s, '        widthClass = "%s";' % (wdths[wdth][1]))
            s = line(s, '    },')

s = line(s, ')')
f = file("%s.txt" % italic[1], "w")
f.write(s)
f.close()

