#!/usr/bin/env bash

fontmake -g SchticksText-MM.glyphs --verbose 'DEBUG' --keep-overlaps --no-production-names -o variable # --use-kern-writer feaLab.writers.kernFeatureNoWriter --use-mark-writer feaLab.writers.markFeatureNoWriter
#mv master_ufo/VotoSerifGX-GX.ttf variable_ttf
#ttx -m variable_ttf/VotoSerifGX-GX.ttf -o variable_ttf_patched/VotoSerifGX.ttf variable_ttf/VotoSerifGX.ttx

fontmake -g SchticksText-MMI.glyphs --verbose 'DEBUG' --keep-overlaps --no-production-names -o variable # --use-kern-writer feaLab.writers.kernFeatureNoWriter --use-mark-writer feaLab.writers.markFeatureNoWriter
#mv master_ufo/VotoSerifGX-GX.ttf variable_ttf
#ttx -m variable_ttf/VotoSerifGX-GX.ttf -o variable_ttf_patched/VotoSerifGX.ttf variable_ttf/VotoSerifGX.ttx

