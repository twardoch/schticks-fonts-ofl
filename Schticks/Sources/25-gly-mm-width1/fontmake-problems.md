
I've just installed the devel `fontmake` on my Mac OS X with Homebrew-installed Python 2.7.13 by running in the repo:

```
pip install --user -r dev-requirements.txt .
pip install --user .
```

so I had:

* booleanOperations-0.6.4
* cu2qu-1.1.2.dev0
* defcon-0.2.1:
* fonttools-3.6.0
* fontmake-1.1.1.dev0
* glyphsLib-1.3.1.dev0
* MutatorMath-2.0.2.dev0
* ufo2ft-0.3.2.dev0

I also did it via

```
pip install --user -r requirements.txt .
pip install --user .
```

So I had

* booleanOperations-0.6.4
* cu2qu-1.1.1
* defcon-0.2.1
* fonttools-3.6.0
* glyphsLib-1.3.0
* MutatorMath-2.0.1
* ufo2ft-0.3.1

In both configurations, when running **fontmake** like this:

```
fontmake -g SchticksText-MM.glyphs --verbose 'DEBUG' --keep-overlaps --production-names -o variable
```

on the `shticks-font/Shticks/25-gly-mm-width1/bak/SchticksText-MM.glyphs` font from my [https://github.com/twardoch/shticks-font](https://github.com/twardoch/shticks-font) repo, I get a number of problems.

## Spurious illegal names

`fontmake` reports one **illegal glyph name** but such a glyph name is not in the font.

```
INFO:fontmake.font_project:Checking Glyphs source for illegal glyph names
WARNING:fontmake.font_project:Found 1 glyph names containing hyphens: B: -219
WARNING:fontmake.font_project:Replacing all hyphens with periods.
```

## com.adobe.type.autohint data

The glyphs contain a custom `com.adobe.type.autohint` entry which makes `glyphsLib` fail. Stuff in `userData` that cannot be parsed should be ignored.

```
userData = {
com.adobe.type.autohint = <ICA8aGludFNldExpc3Q+CiAgICA8aGludHNldCBwb2ludFRhZz0iaHIwMCI+CiAgICAgIDxoc3RlbSBwb3M9Ii0xNjkiIHdpZHRoPSI1MyIgLz4KICAgICAgPGhzdGVtIHBvcz0iLTgiIHdpZHRoPSIxMTUiIC8+CiAgICAgIDxoc3RlbSBwb3M9IjQ2MSIgd2lkdGg9IjIwOCIgLz4KICAgICAgPGhzdGVtIHBvcz0iNjMxIiB3aWR0aD0iMzgiIC8+CiAgICAgIDxoc3RlbSBwb3M9IjczNCIgd2lkdGg9IjUxIiAvPgogICAgICA8dnN0ZW0gcG9zPSIxMCIgd2lkdGg9IjUxIiAvPgogICAgICA8dnN0ZW0gcG9zPSIxMjYiIHdpZHRoPSI3NSIgLz4KICAgICAgPHZzdGVtIHBvcz0iMTI2IiB3aWR0aD0iOTYiIC8+CiAgICAgIDx2c3RlbSBwb3M9IjI0MyIgd2lkdGg9IjExNSIgLz4KICAgICAgPHZzdGVtIHBvcz0iMjgwIiB3aWR0aD0iNDAiIC8+CiAgICAgIDx2c3RlbSBwb3M9IjM5MSIgd2lkdGg9IjkwIiAvPgogICAgICA8dnN0ZW0gcG9zPSI1NDMiIHdpZHRoPSI1MiIgLz4KICAgIDwvaGludHNldD4KICA8L2hpbnRTZXRMaXN0Pgo=>;
};
```

#### Traceback

```
INFO:glyphsLib:Parsing .glyphs file
Traceback (most recent call last):
  File "/Users/adam/Library/Python/2.7/bin/fontmake", line 11, in <module>
    load_entry_point('fontmake', 'console_scripts', 'fontmake')()
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/Lib/fontmake/__main__.py", line 171, in main
    project.run_from_glyphs(glyphs_path, **args)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/Lib/fontmake/font_project.py", line 368, in run_from_glyphs
    glyphs_path, family_name)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/fonttools/Lib/fontTools/misc/loggingTools.py", line 372, in wrapper
    return func(*args, **kwds)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/Lib/fontmake/font_project.py", line 93, in build_master_ufos
    family_name=family_name)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/__init__.py", line 91, in build_masters
    filename, include_instances=True, family_name=family_name)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/__init__.py", line 64, in load_to_ufos
    data = load(file_or_path)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/__init__.py", line 44, in load
    return loads(fp.read())
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/__init__.py", line 53, in loads
    data = p.parse(value)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/parser.py", line 43, in parse
    result, i = self._parse(text, 0)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/parser.py", line 55, in _parse
    return self._parse_dict(text, i)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/parser.py", line 83, in _parse_dict
    res[name], i = self._parse(text, i)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/parser.py", line 61, in _parse
    return self._parse_list(text, i)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/parser.py", line 104, in _parse_list
    list_item, i = self._parse(text, i)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/parser.py", line 55, in _parse
    return self._parse_dict(text, i)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/parser.py", line 83, in _parse_dict
    res[name], i = self._parse(text, i)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/parser.py", line 55, in _parse
    return self._parse_dict(text, i)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/parser.py", line 83, in _parse_dict
    res[name], i = self._parse(text, i)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/parser.py", line 70, in _parse
    self._fail('Unexpected content', text, i)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/parser.py", line 145, in _fail
    raise ValueError('%s:\n%s' % (message, text[i:i + 79]))
ValueError: Unexpected content:
 <ICA8aGludFNldExpc3Q+CiAgICA8aGludHNldCBwb2ludFRhZz0iaHIwMCI+CiAgICAgIDxoc3Rlb
```

## Non-integer underline position

The font contains a weird entry:

```
name = underlinePosition;
value = -77.5;
```

which makes `glyphsLib` fail. I don't know why this entry is there but glyphsLib should round, not fail.

#### Traceback

```
INFO:glyphsLib:Parsing .glyphs file
INFO:glyphsLib:Casting parsed values
Traceback (most recent call last):
  File "/Users/adam/Library/Python/2.7/bin/fontmake", line 11, in <module>
    load_entry_point('fontmake', 'console_scripts', 'fontmake')()
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/Lib/fontmake/__main__.py", line 171, in main
    project.run_from_glyphs(glyphs_path, **args)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/Lib/fontmake/font_project.py", line 368, in run_from_glyphs
    glyphs_path, family_name)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/fonttools/Lib/fontTools/misc/loggingTools.py", line 372, in wrapper
    return func(*args, **kwds)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/Lib/fontmake/font_project.py", line 93, in build_master_ufos
    family_name=family_name)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/__init__.py", line 91, in build_masters
    filename, include_instances=True, family_name=family_name)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/__init__.py", line 64, in load_to_ufos
    data = load(file_or_path)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/__init__.py", line 44, in load
    return loads(fp.read())
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/__init__.py", line 55, in loads
    cast_data(data)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/casting.py", line 510, in cast_data
    _convert_data(data, True, _TYPE_STRUCTURE)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/casting.py", line 526, in _convert_data
    _convert_data(cur_data, to_typed, cur_type)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/casting.py", line 528, in _convert_data
    data[key] = cur_type.convert(data[key], to_typed)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/casting.py", line 78, in convert
    return self.read(data) if to_typed else self.write(data)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/casting.py", line 309, in read
    value = int(value)
ValueError: invalid literal for int() with base 10: '-77.5'
```

## TypeError: int() argument must be a string or a number, not 'list'

After I manually cleaned the offending portions (the font is in `shticks-font/Shticks/25-gly-mm-width1/SchticksText-MM.glyphs`) and run `fontmake` on it, I get:

```
TypeError: int() argument must be a string or a number, not 'list'
```

I have no idea what to do with this, so I cannot proceed any further.

#### Traceback

```
INFO:glyphsLib:Parsing .glyphs file
INFO:glyphsLib:Casting parsed values
Traceback (most recent call last):
  File "/Users/adam/Library/Python/2.7/bin/fontmake", line 11, in <module>
    load_entry_point('fontmake', 'console_scripts', 'fontmake')()
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/Lib/fontmake/__main__.py", line 171, in main
    project.run_from_glyphs(glyphs_path, **args)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/Lib/fontmake/font_project.py", line 368, in run_from_glyphs
    glyphs_path, family_name)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/fonttools/Lib/fontTools/misc/loggingTools.py", line 372, in wrapper
    return func(*args, **kwds)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/Lib/fontmake/font_project.py", line 93, in build_master_ufos
    family_name=family_name)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/__init__.py", line 91, in build_masters
    filename, include_instances=True, family_name=family_name)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/__init__.py", line 64, in load_to_ufos
    data = load(file_or_path)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/__init__.py", line 44, in load
    return loads(fp.read())
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/__init__.py", line 55, in loads
    cast_data(data)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/casting.py", line 510, in cast_data
    _convert_data(data, True, _TYPE_STRUCTURE)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/casting.py", line 526, in _convert_data
    _convert_data(cur_data, to_typed, cur_type)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/casting.py", line 528, in _convert_data
    data[key] = cur_type.convert(data[key], to_typed)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/casting.py", line 78, in convert
    return self.read(data) if to_typed else self.write(data)
  File "/Users/adam/Developer/vcs/github/googlei18n/fontmake/src/glyphslib/Lib/glyphsLib/casting.py", line 136, in read
    return int(src)
TypeError: int() argument must be a string or a number, not 'list'
```

