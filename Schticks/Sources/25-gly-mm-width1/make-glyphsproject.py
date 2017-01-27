#!/usr/bin/env python


class GlyphsProjectGenerator(object): 
    def __init__(self): 

        self.fam = "Schticks Text"
        self.folder = "otf"

        self.projs = { 
            "SchticksText-MM": { 
                "italic":  "" 
            }, 
            "SchticksText-MMI": { 
                "italic": " It"
            }, 
        } 

        self.custs = {
            0: "", 
        }

        self.wghts = {
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

        self.wdths = { 
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

    def makeYamlInstance(self, cust, wdth, wght, italic): 
        l = []
        l.append("-   customParameters:".format())
        l.append("    -   name: preferredFamilyName".format())
        l.append("        value: {0} {1}{2}".format(self.fam, self.custs[cust], self.wdths[wdth][0]))
        l.append("    -   name: preferredSubfamilyName".format())
        l.append("        value: {0}{1}".format(self.wghts[wght][0], italic))
        l.append("    interpolationCustom: {:.1f}".format(cust))
        l.append("    interpolationWeight: {:.1f}".format(wght))
        l.append("    interpolationWidth: {:.1f}".format(wdth))
        if len(italic): 
            l.append("    isItalic: true".format())
        else: 
            l.append("    isItalic: false".format())
        l.append("    name: {0}{1} {2}{3}".format(self.custs[cust], self.wdths[wdth][0], self.wghts[wght][0], italic))
        if len(self.wghts[wght][1]): 
            l.append("    weightClass: {0}".format(self.wghts[wght][1]))
        if len(self.wdths[wdth][1]): 
            l.append("    widthClass: {0}".format(self.wdths[wdth][1]))
        return l

    def makeYamlProlog(self, proj, fmt): 
        l = []
        l.append("exportPath: {0}".format(fmt))
        l.append("fontPath: {0}.glyphs".format(proj, fmt))
        l.append("instances:".format())
        return l

    def makeYamlProject(self, proj, italic): 
        l = []
        l += (self.makeYamlProlog(proj, self.folder))
        for cust in sorted(self.custs.keys()): 
            for wdth in sorted(self.wdths.keys()): 
                for wght in sorted(self.wghts.keys()): 
                    l += (self.makeYamlInstance(cust, wdth, wght, italic))
        return l

    def makeProject(self, proj): 
        l = self.makeYamlProject(proj, self.projs[proj]["italic"])
        yaml = "\n".join(l)
        fn = "{0}.glyphsproject.yaml".format(proj)
        f = file(fn, "w")
        f.write(yaml)
        f.close()
        print("# Saved: {}".format(fn))


    def makeProjects(self): 
        for proj in self.projs: 
            yaml = l = self.makeProject(proj)

gen = GlyphsProjectGenerator()
gen.makeProjects()

