#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function
import sys
import codecs
import os
import pypinyin
import importlib
import re
import math
import LCS as mod13
from itertools import izip

reload(sys)
sys.setdefaultencoding('utf-8')

#openFile
def openFile(dir, fn):
    makeDir(dir)
    output = codecs.open(dir + "/" + fn, mode='w', encoding="GB18030")
    sys.stdout = output

#def openFile(fn):
#    output = codecs.open(fn, mode='w', encoding="GB18030")
#    sys.stdout = output

# readFile
def readFile(fl):
    input = codecs.open(fl, 'r', "GB18030")#以读的方式打开输入文件
    return (input)

def makeDir(dr):
    if(not os.path.exists(dr)):
        os.mkdir(dr)

# Loop 2
def createSmallList(file):
    outting = openFile('debug', 'ddd.txt')
    all = []
    for eachLine in file:       #按行读入文件内容
        temp = eachLine.strip()  # strip()函数是用来删除eachline开头结尾处删除（）里面的字符。
        # if(len(temp)>=10):
        #     continue
        all.append(temp)
    # Get the pinyin of each word from its Chinese form
    # Chinese words are in lists:
    # all (from file menuList.txt.part1, small file)
    # output of loop:
    # names: (array of pinyins for Chinese word)                        (big list)
    # pinyin_unified1: (list of arrays with names, all[index], index)    (all =>  list)
    # names1: (array of pinyins for Chinese word)                           (small list)
    # pinyin_unified2: (list of arrays with names1, all[index], index)      (all => small list)
    #########
    return all

# def wordsInline(object):
#     inlinesWords = openFile("wordsinline.txt")
#     inlines = []
#     for eachline in object:
#        words = eachline.replace(" ", "\n")
#        # words2 = words.rstrip("\n")
#        inlines.append(words)

#
# for i in inlines:
#     print(i)


def getminIndex(object):
    minIndex = 0
    minIndex = len(object)
    return minIndex

# Loop 3
#input: sorted pinyin list
#output: associated array with pinyin as key
# pinyin_unified2 has elements of type (names1, all[index], index)
def chineseToPinyin(all):  # 转换中文菜名到拼音形式
    output1 = openFile("pinyin","pinyin.txt")
    pinyin_unified2 = []
    for index in range(getminIndex(all)):
        name1 = 0;
        try:
            name1 = pypinyin.slug(all[index], separator=u' ')
        except:
            print("Unexcepted error: ")
            raise
        names1 =name1.split(" ")
        pinyin_unified2.append([names1, all[index], index])
    # print(pinyin_unified2)
    return (pinyin_unified2)

# loop 3_2
def chineseToPinyinShengm(all):  # 转换中文菜名到声母形式
    output1_2 = openFile("result","PinyinShengm.txt")
    shengm_unified = []
    for index in range(getminIndex(all)):
        shengm1 = 0;
        try:
            shengm = pypinyin.slug(all[index], separator=u' ', style=pypinyin.INITIALS)
        except:
            print("Unexcepted error: ")
            raise
        shengm1=shengm.split(" ")
        shengm_unified.append([shengm1, all[index], index])
    # print(shengm_unified2)
    return(shengm_unified)

#loop3_3
def chineseToPinyinYunm(all):  # 转换中文菜名到韵母形式
    output1_3 = openFile("result","PinyinYunm.txt")
    yunm_unified = []
    for index in range(getminIndex(all)):
        yunm1 = 0;
        try:
            yunm = pypinyin.slug(all[index], separator=u' ', style=pypinyin.FINALS)
        except:
            print("Unexcepted error: ")
            raise
        yunm1 = yunm.split(" ")

        yunm_unified.append([yunm1, all[index], index])
    # print(yunm_unified)
    return(yunm_unified)

# Loop 4
#######################
#   Now use the pinyin_unified2 (from list "all", the small one)
#   from loop 3 (The previous loop).
#   Task:
#   To find words that have at least two pinyin in common
#   Output:
def printEnumeratedPinyin(pinyin_unified):  # 转换成排好序的拼音
    output2 = openFile("result","enumeratePinyin.txt")
    #    enum, pinyin_unified_enum = enumerate(pinyin_unified2)
    #    for (i, (compArrA, origWord1, origIndex)) in pinyin_unified_enum:
    # for i, elem in enumerate(pinyin_unified2):
    #     print("compArrA:", i, elem)
        #    for (compArrA, origWord1, origIndex), elem in pinyin_unified_enum:
        #        print("compArrA:", (compArrA, origWord1, origIndex), "\n")
        #    for i, elem in pinyin_unified_enum:
        #        print("compArrA:", i, elem, "\n")


#loop 4_1
def printEnumeratedShengm(shengm_unified):  # 转换成排好序的声母
    output2_1 = openFile("result","enumeratePinyinShengm.txt")
    # for i, elem in enumerate(shengm_unified2):
    #     print("compArrA:", i, elem)

#loop 4_2
def printEnumerateYunm(yunm_unified):  # 转换成排好序的韵母
    output2_2 = openFile("result","enumeratePinyinYunm.txt")
    # for i, elem in enumerate(yunm_unified2):
    #     print("compArrA:", i, elem)
#loop 5
def createSortedPinyin(pinyin_unified):  # 创建排序了的拼音
    output3 = openFile("result","sortedPinyin.txt")
    pinyin_unified_sorted = sorted(pinyin_unified, key=lambda x: x[1])
    pinyin_unified_sorted_enum = enumerate(pinyin_unified_sorted)
       # for i, (compArrA, origWord1, origIndex) in pinyin_unified_sorted_enum:
       #     print("compArrA:", i, compArrA, origWord1, origIndex)
    for i, elem in pinyin_unified_sorted_enum: # print("compArrA:", elem)
      return pinyin_unified_sorted

#loop 5_1
def createSortedShengm(shengm_unified):  # 创建排序了的声母
    output3_1 = openFile("result","sortePinyinShengm.txt")
    shengm_unified_sorted = sorted(shengm_unified, key = lambda x: x[1])
    shengm_unified_sorted_enum = enumerate(shengm_unified_sorted)
    # for i, elem in shengm_unified_sorted_enum:
    #     print("compArrA:", elem)
    return shengm_unified_sorted

#loop 5_2
def createSortedYunm(yunm_unified):  # 创建排序了的韵母
    output3_2 = openFile("result","sortePinyinYunm.txt")
    yunm_unified_sorted = sorted(yunm_unified, key = lambda  x: x[1])
    yunm_unified_sorted_enum = enumerate(yunm_unified_sorted)
    # for i, elem in yunm_unified2_sorted_enum:
    #     print("compArrA:", elem)
    return yunm_unified_sorted

# Loop 6
def createPinyinAssociatedArray(pinyin_unified_sorted):  # 创建排好序的[拼音， unicode， 下标序号]
    output4 = openFile("result","PinyinAssociatedArray.txt")
    assArrA = {}
    # print("total number of pinyins:", len(pinyin_unified_sorted))
    pinyin_unified_sorted_enum = enumerate(pinyin_unified_sorted)

    # for i, elem in pinyin_unified_sorted_enum:
    #     print("pinyin_unified_sorted_enum", elem)

    output5 = openFile("result","out.txt")  # 打印出[序号， 拼音， unicode， 下标序号] 中文菜名
    # print("started looping pinyin_unified_sorted")
    for i, (compArrA, origWord, origIndex) in enumerate(pinyin_unified_sorted):
        pinyinString = "_".join(compArrA)

        # print("pinyinString:", pinyinString, compArrA)

        if(not pinyinString in assArrA.keys()):
            assArrA[pinyinString] = [[i, (compArrA, origWord, origIndex)]]
        else:
            assArrA[pinyinString].append([i, (compArrA, origWord, origIndex)])  # add the same pinyin food name in same line
        # print("%s" % assArrA[pinyinString], origWord)
    return assArrA


# loop 6_1

def createShengmAssociatedArray(shengm_unified_sorted):  # 用于创建并打印[首个声母, unicode, 下标序号]
    output4_1 = openFile("result","ShengmAssociatedArray.txt")
    assArrA1 = {}
    # print("total number of shengm:", len(shengm_unified_sorted))
    shengm_unified_sorted_enum = enumerate(shengm_unified_sorted)
    #
    # for i, elem in shengm_unified_sorted_enum:
    #     print("shengm_unified_sorted_enum", elem)


    output6 = openFile("result","outShengm.txt")  # 打印 [序号， 首个声母， unicode， 下标序号] 对应的中文菜名
    for i, (compArrA, origWord, origIndex) in enumerate(shengm_unified_sorted):
        shengmString = "_".join(compArrA)
        # print("-"*30)
        if(not shengmString in assArrA1.keys()):

            assArrA1[shengmString] = [[i, (compArrA, origWord, origIndex)]]
        else:
            assArrA1[shengmString].append([i, (compArrA, origWord, origIndex )])
        # print("%s"%assArrA1[shengmString], origWord)
    return assArrA1



# loop 6_2

def createYunmAssociatedArray(yunm_unified_sorted):  # 用于创建并打印[首个韵母, unicode, 下标序号]
    output4_2 = openFile("result","YunmAssociatedArray.txt")
    assArrA2 = {}
    # print("total number of yunm:", len(yunm_unified_sorted))
    yunm_unified_sorted_enum = enumerate(yunm_unified_sorted)

    for i, elem in yunm_unified_sorted_enum:
        # print("yunm_unified_sorted_enum", elem)


        output6 = openFile("result","outYunm.txt")  # 打印 [序号， 首个韵母， unicode， 下标序号] 对应的中文菜名
    for i, (compArrA, origWord, origIndex) in enumerate(yunm_unified_sorted):
        yunmString = "_".join(compArrA)
        # print("-"*30)
        if(not yunmString in assArrA2.keys()):

            assArrA2[yunmString] = [[i, (compArrA, origWord, origIndex)]]
        else:
            assArrA2[yunmString].append([i, (compArrA, origWord, origIndex )])
        # print("%s"%assArrA2[yunmString], origWord)
    return assArrA2


 # loop
def normalizeShengm(shengm_unified):  # 用于定义相等的声母和在整个菜名寻找所有的声母并替换所有相等的声母为定义好的相等集合里面的第一个位置的值， 并一一打印出来和对应的中文和序号等
    openFile("result", "shengmWithNormal.txt")
    shengm_set = [['z', 'zh'], ['s', 'sh'], ['c', 'ch'], ['l', 'r'], ['f', 'h'], ['n', 'm'], ['b', 'p'], ['d', 't']]
    shengm_unified_normal = []

    for row in shengm_unified:
        normal_row = []
        # print ("testing row:", row)
        array = row[0]
        #        for array in row:
        # print ("testing array:", array)
        #            if not type(array) is list:
        #                array = [array]
        for elem in array:

            foundMatch = 0
            for s in shengm_set:
                # print('elem: ', elem, 'shengm:', s)
                if(elem in s):
                    # print('match')
                    foundMatch = 1
                    normal_row.append(s[0])
            if(not foundMatch):
                normal_row.append(elem)

            # print("normalized:",row[0], normal_row, row[1], row[2])
        shengm_unified_normal.append([row[0], normal_row, row[1], row[2]])

    return shengm_unified_normal

def normalizeYunm(yunm_unified):  # 用于定义相等的韵母和在整个菜名寻找所有的韵母并替换所有相等的声母为定义好的相等集合里面的第一个位置的值， 并一一打印出来和对应的中文和序号等
    outyunm = openFile("result","yunmWithNormal.txt")
    yunm_set = [['a', 'ai', 'ia', 'uai'],['iu', 'ui', 'iou', 'uei'], ['ün', 'un', 'uen'],
                ['i', 'v', 'ü'],
                ['ian', 'uan', 'uang', 'ang', 'an', 'iang', 'üan'], ['ueng', 'eng', 'en', 'e', 'ei', 'ie','iei'],
                ['uong', 'ong', 'on', 'iong', 'o', 'ou'],
                ['uo', 'u', 'ua'], ['iao', 'ao']]
    yunm_unified_normal = []

    for row in yunm_unified:
        normal_row = []
        # print('testing row:', row)
        array = row[0]
        # print('testing array:', array)
        #        if not type(array) is list:
        #            array = [array]
        for elem in array:

            foundMatch = 0
            for s in yunm_set:
                # print('elem: ', elem, 'shengm:', s)
                if(elem in s):
                    # print('match')
                    foundMatch = 1
                    normal_row.append(s[0])
            if(not foundMatch):
                normal_row.append(elem)  #  if it has test all shengm_set and didn't find match, should just append elem
        print('normalized:', row[0], normal_row, "row:", row[1], row[2])
        yunm_unified_normal.append([row[0], normal_row, row[1], row[2]])

    return yunm_unified_normal

def sameName(shengm_unified_normal, yunm_unified_normal):  # 结合声母和韵母， 首先分别替换成同一个集合里面定义好的第一个位置的声母或者韵母， 然后再结合替换后的声母和韵母， 并打印出来
    outSameNm = openFile("result","sameName.txt")
    normalized_sh_yun = []

    for shengmGroup, yunmGroup in izip(shengm_unified_normal, yunm_unified_normal):
        shengmArr = shengmGroup[1]
        yunmArr = yunmGroup[1]

        # print('shengm:',shengmGroup, 'yunm:',yunmGroup)
        normalized_sh_yun_word = []

        for shengm, yunm in izip(shengmArr, yunmArr):
             shengm = shengm.decode('utf-8')
             yunm = yunm.decode('utf-8')
             # print(shengm, yunm)
             joinedString = "".join([shengm, yunm])
             # print(shengm, yunm, joinedString)
             normalized_sh_yun_word.append(joinedString)

        normalized_sh_yun.append([normalized_sh_yun_word, shengmGroup, yunmGroup])

    for elem in normalized_sh_yun:
        print('elem: ',elem)

        return normalized_sh_yun

# getting pinyin
def getPinyin(pinyin_unified, shengm_unified, yunm_unified):  # 整合一个集合里面有原始的拼音和声母， 韵母。
    normalized_py_sh_yun = []
    for pinyin, shengm, yunm in izip(pinyin_unified, shengm_unified, yunm_unified):
        normalized_py_sh_yun.append([pinyin, shengm, yunm])

    return normalized_py_sh_yun

# loop 6_3
def createChangedPinyinAssociatedArray(changed_pinyin_unified_sorted):  # 使用字典， 找出排好序的菜名（已经替换好了声母和韵母的）
    output4_3 = openFile("result","PinyinShengmAssociatedArray.txt")
    assArrA3 = {}

# assArrA3 like this structure:
# data from function createChangedPinyinAssociatedArray
#  index  [0]
#     i
#  tuple [1]
#    changedPinyinArr  [1][0]
#        array of changed pinyin
#    shengm            [1][1]
#        array of shengm
#    yunm
#        array of yunm


    # print("total number of changed pinyin:", len(changed_pinyin_unified_sorted))
    changed_pinyin_unified_sorted_enum = enumerate(changed_pinyin_unified_sorted)

    for i, elem in changed_pinyin_unified_sorted_enum:
        print("changed_pinyin_unified_sorted_enum", elem)

        output6 = openFile("result","outChangedPinyin.txt")

    for i, (changedPinyinArr,shengm, yunm) in enumerate(changed_pinyin_unified_sorted):
        changed_pinyin_String = "_".join(changedPinyinArr)
        if not (changed_pinyin_String) in assArrA3.keys():
            assArrA3[changed_pinyin_String] = [[i, (changedPinyinArr,shengm, yunm)]]
        else:
            assArrA3[changed_pinyin_String].append([i, (changedPinyinArr, shengm, yunm)])
    # print(assArrA3)
    return assArrA3

def createChangedPinyinShengmYunmAssociatedArray(pinyinShengmYunm_unified_normal):  # 使用字典， 找出排好序的菜名（拼音，声母和韵母）
    output4_4 = openFile("result","PinyinShengmYunmAssociatedArray.txt")
    assArrA4 = {}
    print("total number of pinyin:", len(pinyinShengmYunm_unified_normal))
    pinyinShengmYunm_unified_normal_enum = enumerate(pinyinShengmYunm_unified_normal)

    output6 = openFile("result","outChangedPinyinShengmYunm.txt")



    for i, (pinyinGroup, shengmGroup, yunmGroup) in enumerate(pinyinShengmYunm_unified_normal):
        pinyinWord = pinyinGroup[0]  # it has three elements which each contains 3 elements in turn
        pinyinOrig = pinyinGroup[1]  # pinyin contains the slug, the original form and the index from the "all" list
        pinyinIndex = pinyinGroup[2]

    for i,elem in enumerate(pinyinShengmYunm_unified_normal):
        print("changed_pinyin_unified",elem)

# like create following structure assArrA4:
# data from function createChangedPinyinShengmYunmAssociatedArray
# pinyinGroup [0]
#   pinyinWord[0][0]
#   pinyinOrig[0][1]
#   pinyinIndex[0][2]
# shengmGroup [1]
#   shengmWord [1][0]
#   shengmOrig [1][1]
#   shengmIndex[1][2]
# yunmGroup [2]
#    yunmWord[2][0]
#    yunmOrig[2][1]
#    yunmIndex[2][2]


        pinyin_String = "_".join(pinyinWord)
        if not (pinyin_String) in assArrA4.keys():
            assArrA4[pinyin_String] = [[i, (pinyinGroup, shengmGroup, yunmGroup)]]
        else:
            assArrA4[pinyin_String].append([i, (pinyinGroup, shengmGroup, yunmGroup)])
    return assArrA4


# Loop 7
# def createSmallResultFiles(assArrA):
#
#     openFile("result", "smallResFile.txt")
#     makeDir("pinyins")
#     with codecs.open("pinyins/result.txt", mode='w', encoding="utf-8") as f:
#
#         for key in assArrA:
#             origWord_set = set()
#
#             for i, (compArrA, origWord1, origIndex) in assArrA[key]:
#                 origWord_set.add(origWord1)
#             setSize = len(origWord_set)
#
#             # print('---',setSize, '====',key, '++=',origWord_set)
#
#             if(setSize <= 1):
#                 continue

            # print("passed")
            #outstring = "".join(["Chinese forms in dict:", str(origWord_set), "\n"])
            # outstring = "".join([str(origWord_set), "\n"])
            #
            # outstring = outstring.encode("utf-8")
            #
            # f.write (str(outstring))

            # for elem in assArrA[key]:
            #     #outstring = "".join(["compArrA:", str(elem), "\n"])
            #     outstring = "".join([str(elem), "\n"])
            #     outstring = outstring.encode("utf-8")
            #     f.write(str(outstring))

def createSmallResult(assArrA3, assArrA4):  # 一一比较字典里的拼音， 声母， 韵母， 排序好并且比较替换好了声母和字母后相等的就显示passed并打印出来（即要找的相等的菜名）

    openFile("result", "smallResShengmYunm.txt")
    makeDir("ShengmYunm")
    with codecs.open("ShengmYunm/result.txt", mode='w', encoding="utf-8") as f:

        for key in assArrA3:
            shengm_set = set()
            shengsetString = str(shengm_set)  # encode()

            for i, (changedPinyinArr,shengm, yunm) in assArrA3[key]:
                # print('8'*30)
                # print(changedPinyinArr, shengm, yunm)
                # sys.stdout.flush()
                shengm_set.add(shengm[2])  # shengm[2] is the origianl Chimese word

            setSize = len(shengm_set)
            # print(setSize, "key:", key, "set:", shengm_set, "changedPinyinArr:", changedPinyinArr)

            # outstringDbg = "".join([str(setSize), " key:", str(key), " set:", str(shengm_set), " changedPinyinArr:", str(changedPinyinArr)])



            if(setSize <= 1):
                continue

            outstringDbg = "\n".join(shengm_set)
            print(outstringDbg)



            # for elem in shengm_set:
            #     print (str(elem).encode(encoding='utf-8'))
            #     print("passed")
        # -----------------------------------------------------------------------------------------------------------
        # for key in assArrA4:
        #     psy_set = set()
        #     psysetString = str(psy_set)
        #
        #
        #     for i, ([pinyinGroup, shengmGroup, yunmGroup]) in assArrA4[key]:
        #         pinyinWord = pinyinGroup[0]  # it has three elements which each contains 3 elements in turn
        #         pinyinOrig = pinyinGroup[1]  # pinyin contains the slug, the original form and the index from the "all" list
        #         pinyinIndex = pinyinGroup[2]
        #
        #         print("")
        #         for elem in pinyinGroup[0]:
        #             print(elem)
        #         print(pinyinGroup[1])
        #         print(pinyinGroup[2])
        #
        #         for elem in shengmGrouo[0]:
        #             print(elem)
        #         print(shengmGroup[1])
        #         print(shengm_set[2])
        #
        #         for elem in yunmGroup[0]:
        #             print(elem)
        #         print(yunmGroup[1])
        #         print(yunmGroup[2])
        #
        #         sys.stdout.flush()


                # print(pinyinGroup, shengmGroup, yunmGroup)
                # sys.stdout.flush()
                # psy_set.add(pinyinOrig)

            # setSize = len(psy_set)
            #
            # outstringDbgForAll = "".join(["ass4:", str(setSize), " key:", str(key), " set:", str(psy_set), " pinyin:", str(pinyinGroup)])
            # # print(outstringDbgForAll)
            #
            # if(setSize <= 1):
            #     continue
            #
            # print ("passed")
            # outstring = "".join(["shengm_set: ", str(shengm_set), "\n"]) + "".join(["psy_set:", str(psy_set), "\n"])
            # outstring = outstring.encode("utf-8")
            # f.write (str(outstring))

def Similarity(a,b): #getting the similarity from the LCS
    k = mod13.find_lcs_len(a,b)/math.sqrt(len(a)*len(b) )
    print("similarity: ", k)
    return k

def loopforList(all):  # 对于相似度定义一个阀值， 并打印出来
    openFile("result","outPutForLoopforTwowords.txt")
    Ass = {}
    for wordA in all:
        for wordB in all:
            if wordA == wordB:
                continue
            wordA_set = set(wordA)
            wordB_set = set(wordB)
            if (len(wordA_set.intersection(wordB_set))<=2): #Getting the food name if there are immonen letters more than 2
                continue
            Similarity(wordA, wordB)

            if Similarity(wordA, wordB) >=0.81: #setting an threshold value which is 0.93
                print(wordA , wordB)

                # print(wordA + '\n' + wordB)



def GettingWordsNone(all, firstForPinyin, secondLoop):  # 求差集的一些步骤
    output00 = openFile("result","Byline.txt")
    # i = set(forexample)
    # l = set(wordInline)
    # removed = i.union(l)
    # print(removed)
    #set(list(set(wordInline).union(set(forexample))))
    # removed = list(set(all).difference(set(list(set(firstForPinyin).union(set(secondLoop))))))  # 求差集， 即： all中有的， 而allpinyin和allsimilar中没有的
    # for k in removed:
    #     print(k)
