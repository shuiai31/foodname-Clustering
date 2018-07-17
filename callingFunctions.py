#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import sys
import importlib
from re import compile as _Re

_unicode_chr_splitter = _Re( '(?s)((?:[\ud800-\udbff][\udc00-\udfff])|.)').split

def split_unicode_char(text):
    return [ chr for chr in _unicode_chr_splitter(text) if chr ]


import functions as mod6

fin = mod6.readFile("menuList.txt")
# Noinclude = mod6.readFile("notincluein.txt")
# pinyin = pinyininLines1 = mod6.readFile("LineByLInePyShmYum.txt")
# similar = outPutForLoop2 = mod6.readFile("secondLoop.txt")
all = mod6.createSmallList(fin)
# firstForPinyin = mod6.createSmallList(pinyin)
# secondLoop = mod6.createSmallList(similar)

# wordInline = mod6.readFile("short.txt")
# forexample = mod6.readFile("long.txt")

# mod6.GettingWordsNone(forexample, wordInline)

pinyin_unified = mod6.chineseToPinyin(all)
shengm_unified = mod6.chineseToPinyinShengm(all)
yunm_unified = mod6.chineseToPinyinYunm(all)

pinyin_unified_sorted = mod6.createSortedPinyin(pinyin_unified)
shengm_unified_sorted = mod6.createSortedShengm(shengm_unified)
yunm_unified_sorted = mod6.createSortedYunm(yunm_unified)

assArrA = mod6.createPinyinAssociatedArray(pinyin_unified_sorted)
assArrA1 = mod6.createShengmAssociatedArray(shengm_unified_sorted)
assArrA2 = mod6.createYunmAssociatedArray(yunm_unified_sorted)

shengm_unified_normal = mod6.normalizeShengm(shengm_unified)
yunm_unified_normal = mod6.normalizeYunm(yunm_unified)

changed_unified_normal = mod6.sameName(shengm_unified_normal, yunm_unified_normal)
pinyinShengmYunm_unified_normal = mod6.getPinyin(pinyin_unified, shengm_unified, yunm_unified)

assArrA3 = mod6.createChangedPinyinAssociatedArray(changed_unified_normal)
assArrA4 = mod6.createChangedPinyinShengmYunmAssociatedArray(pinyinShengmYunm_unified_normal)

# mod6.createSmallResultFiles(assArrA)
ww=mod6.createSmallResult(assArrA3, assArrA4)

# shengm_unified = mod6.chineseToPinyin(all)
# mod6.printEnumeratedShengm(shengm_unified)
# shengm_unified_sorted = mod6.createSortedShengm(shengm_unified)
# assShengmArrA = mod6.createShengmAssociatedArray(shengm_unified_sorted)

mod6.loopforList(ww)

# mod6.ResultFiles(Ass)

# mod6.GettingWordsNone(all, firstForPinyin, secondLoop)
sys.stdout = sys.__stdout__
# output.close()


