# Schticks Text Font Family

**Schticks Text** is an OFL-licensed font family, developed as an extensive fork of the renowned **STIX Two Text** fonts. Designed for versatility, it caters to typographers, publishers, and designers seeking a classic yet comprehensive text typeface suitable for a wide array of applications, including scientific, medical, and technical publications, as well as general-purpose text setting.

The family significantly expands upon STIX Two Text by offering a broad spectrum of weights and widths, providing enhanced typographic flexibility. While rooted in a design optimized for scholarly content, Schticks Text's expanded range makes it a robust choice for diverse design challenges.

**Note:** All fonts in the Schticks Text family are currently experimental, unfinished, and not recommended for production use. They are subject to change, and known issues include misaligned diacritics and some inconsistent spacing.

<p align="center">
  <img src="Schticks/Media/png/SchticksText-1UlCd100Th.png" alt="Schticks Text Ultra Condensed Thin" width="30%"/>
  <img src="Schticks/Media/png/SchticksText-5No400Rg.png" alt="Schticks Text Normal Regular" width="30%"/>
  <img src="Schticks/Media/png/SchticksText-9UlWd900Blk.png" alt="Schticks Text Ultra Wide Black" width="30%"/>
</p>
<p align="center">
  <em>Samples (left to right): Schticks Text Ultra Condensed Thin, Normal Regular, Ultra Wide Black</em>
</p>

## Key Features

*   **Expanded Range:** Offers a significantly wider selection of weights (Thin to Black) and widths (Ultra Condensed to Ultra Wide) compared to STIX Two Text.
*   **OpenType Savvy:** Builds upon STIX Two's rich OpenType feature set.
*   **Comprehensive Character Set:** Inherits STIX Two's extensive glyph coverage, including Latin, Greek, and Cyrillic scripts.
*   **Open Source:** Fonts are licensed under the SIL Open Font License (OFL 1.1), and accompanying tools/scripts are under Apache License 2.0.

## Comparison with STIX Two Text

Schticks Text originates from **STIX Two Text** (Version 2.0.0), a project by Tiro Typeworks that modernized the Times Roman model for digital typography. STIX Two Text includes Regular, Italic, Bold, and Bold Italic styles, along with a dedicated Math font. You can find the original STIX Two Text files (v2.0.0) in the [`STIXv2/`](STIXv2/) directory of this repository for reference.

The primary enhancement Schticks Text brings is the vast expansion in weights and widths, transforming the core STIX Two Text design into a more versatile superfamily.

## Downloads & Installation

*   **Desktop Fonts (OTF):** [Download Schticks Text OTF package (163 fonts, v102.000)](https://github.com/twardoch/schticks-fonts-ofl/raw/master/Schticks/Fonts/SchticksText-OTF.zip)
*   **Desktop Fonts (TTF):** [Download Schticks Text TTF package (163 fonts, v102.000)](https://github.com/twardoch/schticks-fonts-ofl/raw/master/Schticks/Fonts/SchticksText-TTF.zip)
*   **Full Repository (for developers):** [Download entire repository ZIP](https://github.com/twardoch/schticks-fonts-ofl/archive/master.zip)

To install the fonts, download either the OTF or TTF package, unzip it, and install the font files using your operating system's standard font management tools.

## Using Schticks Text

For most users, Schticks Text fonts can be selected and used in any application that allows font choice, such as word processors, design software, or web pages (using appropriate web font formats if self-hosting).

For developers wishing to build or modify the fonts, please see the "Technical Details" section below.

### Specimens & Visuals

*   [Schticks Text Overview PDF](https://github.com/twardoch/schticks-fonts-ofl/raw/master/Schticks/Media/Schticks-Text-Overview.pdf)
*   [Schticks Text Specimen PDF](https://github.com/twardoch/schticks-fonts-ofl/raw/master/Schticks/Media/Schticks-Text-Specimen.pdf)
*   [Schticks Text Glyph Set PDF](https://github.com/twardoch/schticks-fonts-ofl/raw/master/Schticks/Media/Schticks-Text-Glyphset.pdf)
*   [Browse all PNG Samples](Schticks/Media/)

## Font Details

### Available Styles
Schticks Text provides an extensive array of styles, currently comprising 163 individual fonts across its OpenType (OTF) and TrueType (TTF) families. The styles span multiple axes, systematically named:

*   **Weight:** Ranges from Thin (100) to Black (900). The full sequence is:
    *   `100Th` (Thin)
    *   `200ExLt` (ExtraLight)
    *   `300Lt` (Light)
    *   `400Rg` (Regular)
    *   `500Md` (Medium)
    *   `600SmBd` (SemiBold)
    *   `700Bd` (Bold)
    *   `800ExBd` (ExtraBold)
    *   `900Blk` (Black)
*   **Width:** Offers nine variations from Ultra Condensed (1) to Ultra Wide (9):
    *   `1UlCd` (Ultra Condensed)
    *   `2ExCd` (Extra Condensed)
    *   `3Cd` (Condensed)
    *   `4SmCd` (SemiCondensed)
    *   `5No` (Normal)
    *   `6SmWd` (SemiWide)
    *   `7Wd` (Wide)
    *   `8ExWd` (ExtraWide)
    *   `9UlWd` (UltraWide)
*   **Slope:** Each weight/width combination is available in both Roman (e.g., `SchticksText-5No400Rg.otf`) and Italic (e.g., `SchticksText-5No400RgIt.otf`).

This systematic naming (e.g., `SchticksText-1UlCd100Th.otf` for Ultra Condensed Thin) results in the full family of 9 widths x 9 weights x 2 slopes = 162 styles (plus potentially a base style if not counted in these, though 163 suggests one extra variant or a slight deviation in total count).

### Glyph Coverage
Inheriting from STIX Two Text, Schticks Text boasts comprehensive Unicode character support, particularly for:
*   Latin-based scripts
*   Greek
*   Cyrillic

It includes features such as true small capitals (for Latin, Greek, and Cyrillic), various numeral styles (lining, oldstyle, proportional, tabular), fractions, and sub/superscripts. For a detailed look at the glyph inventory, please consult the [Schticks Text Glyph Set PDF](https://github.com/twardoch/schticks-fonts-ofl/raw/master/Schticks/Media/Schticks-Text-Glyphset.pdf).

### OpenType Features
Schticks Text supports a rich set of OpenType typographic features, largely inherited from STIX Two Text. These include (feature tags in `code`):
*   `c2sc`: Small Capitals From Capitals
*   `case`: Case-Sensitive Forms
*   `ccmp`: Glyph Composition/Decomposition
*   `cv01`, `cv02`: Character Variants (e.g., lambda with horizontal crossbar, serifed ramshorn)
*   `dnom`: Denominators
*   `frac`: Fractions (diagonal)
*   `kern`: Kerning
*   `liga`: Standard Ligatures (e.g., fi, fl)
*   `numr`: Numerators
*   `onum`: Oldstyle Figures
*   `pnum`: Proportional Figures
*   `smcp`: Small Capitals
*   `subs`: Subscript
*   `sups`: Superscript
*   `ss01`: Stylistic Set 1 (alternate lowercase 'g' in Italic styles)

*This list is based on STIX Two Text features; specific implementation in Schticks Text should be verified by testing in OpenType-aware applications.*

## Technical Details (For Font Developers)

### Font Generation Process
Schticks Text began as a fork of the STIX Two Text OpenType fonts (Regular, Italic, Bold, Bold Italic). Adam Twardoch then modified and significantly expanded these base designs, primarily by creating multiple-master sources to interpolate the extensive range of weights and widths that characterize the Schticks Text family.

The font sources are primarily in the `.glyphs` file format (used by the Glyphs font editor). The most current master source files for generating variable fonts and static instances appear to be:
*   `Schticks/Sources/25-gly-mm-width1/SchticksText-MM.glyphs` (Roman)
*   `Schticks/Sources/25-gly-mm-width1/SchticksText-MMI.glyphs` (Italic)

A shell script, `Schticks/Sources/25-gly-mm-width1/make-varfonts.sh`, demonstrates the use of `fontmake` (a command-line tool for building fonts from UFOs or Glyphs sources) to compile variable TrueType fonts:
```bash
# Example from make-varfonts.sh:
fontmake -g SchticksText-MM.glyphs --verbose 'DEBUG' --keep-overlaps --no-production-names -o variable
fontmake -g SchticksText-MMI.glyphs --verbose 'DEBUG' --keep-overlaps --no-production-names -o variable
```
The static OTF and TTF instances provided in the download packages are likely generated from these master sources, either via the variable font workflow or through direct export capabilities of font design software.

### Source File Structure
*   **`Schticks/Sources/`**: This directory contains the core development files for Schticks Text.
    *   `25-gly-mm-width1/`: Holds the primary GlyphsApp master source files (`.glyphs`) and build scripts for the current iteration of the family.
    *   Other numbered subdirectories (e.g., `01-orig-otf/`, `10-vfb-mm/`, `41-otf-tr/`) represent various stages in the font's development history, potentially including older FontLab VFB sources and intermediate build outputs.
*   **`Schticks/Fonts/`**: Contains the distributable font files (OTF and TTF).
*   **`Schticks/Media/`**: Contains specimen documents (PDFs) and PNG image samples.
*   **`STIXv2/`**: Contains the original STIX Two font files (Version 2.0.0) and their documentation, serving as the upstream basis for Schticks Text.

## Contributing

As an open-source project, contributions to Schticks Text are welcome! Given the experimental nature of the fonts, assistance in refining them is particularly appreciated.

### Reporting Issues
Please report any bugs, rendering issues, or suggestions through the [GitHub Issues tracker](https://github.com/twardoch/schticks-fonts-ofl/issues). Be sure to include details about the font version, operating system, application used, and steps to reproduce the issue.

### Making Contributions
1.  Fork the repository.
2.  Make your changes in a new branch. Adhere to the existing design style and ensure consistency.
3.  If modifying font sources, familiarize yourself with the GlyphsApp format and the `fontmake` build process.
4.  Submit a pull request with a clear description of your changes.

### License
*   **Schticks Text Fonts:** Licensed under the [SIL Open Font License, Version 1.1](./fonts.LICENSE).
    *   You are free to use, study, modify, and redistribute the fonts.
    *   They cannot be sold by themselves.
    *   Modified versions must be released under the OFL and must use a different Reserved Font Name.
*   **Build Scripts & Documentation:** Licensed under the [Apache License, Version 2.0](./other.LICENSE).

## Credits

*   **Schticks Text Modification and Expansion:** Adam Twardoch
*   **STIX Two Design:** Ross Mills (Tiro Typeworks Ltd.), with contributions from MicroPress Inc., and final additions/corrections by Coen Hoffman (Elsevier, retired).
*   **Original STIX Project Initiative:** The STI Pub Companies (American Chemical Society, American Institute of Physics, American Mathematical Society, American Physical Society, Elsevier Inc., and The Institute of Electrical and Electronic Engineers, Inc.).

## Development Notes & Known Issues

The following notes reflect the development status and known challenges, some ofwhich date back to January 2017:

*   **Variable Font Generation Challenges:** The document [`Schticks/Sources/fontmake-problems.md`](Schticks/Sources/fontmake-problems.md) details several issues encountered with `fontmake` and `glyphsLib` during attempts to build variable fonts. These included spurious illegal glyph name warnings, problems with custom `com.adobe.type.autohint` data, non-integer underline positions in Glyphs source, and various TypeErrors during parsing. While the `make-varfonts.sh` script indicates current efforts to build variable fonts, these historical notes provide context on potential tooling sensitivities.
*   **Glyph Compatibility:** "Two glyphs not compatible after MM: `uni025F` and `uni02A6`." (January 2017)
*   **General Status:** As stated, the fonts are experimental. Users should anticipate imperfections such as misaligned diacritics or suboptimal spacing in certain glyph combinations.

## Original STIX Project Description (Historical Context)

> Arie de Ruiter, who in 1995 was Head of Information Technology Development at Elsevier Science, made a proposal to the STI Pub group, an informal group of publishers consisting of representatives from the American Chemical Society (ACS), American Institute of Physics (AIP), American Mathematical Society (AMS), American Physical Society (APS), Elsevier, and Institute of Electrical and Electronics Engineers (IEEE). De Ruiter encouraged the members to consider development of a series of Web fonts, which he proposed should be called the Scientific and Technical Information eXchange, or STIX, Fonts. All STI Pub member organizations enthusiastically endorsed this proposal, and the STI Pub group agreed to embark on what has become a twelve-year project. The goal of the project was to identify all alphabetic, symbolic, and other special characters used in any facet of scientific publishing and to create a set of Unicode-based fonts that would be distributed free to every scientist, student, and other interested party worldwide. The fonts would be consistent with the emerging Unicode standard, and would permit universal representation of every character. With the release of the STIX fonts, de Ruiter's vision has been realized.

*STIX Fonts™ is a trademark of The Institute of Electrical and Electronics Engineers, Inc.*

---

This README aims to provide comprehensive information for both users and potential contributors to the Schticks Text font family.
