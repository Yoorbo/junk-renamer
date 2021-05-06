import os
import random
files = os.listdir()
words = open("C:\everyenglishword.txt").read().splitlines()
filenamearray = []
filename = " "
for x in files:
    possiblename = random.choice(words)
    name = x.lower()
    try:
        no720p = name.replace("-720p", "")
    except:
        no720p = name.replace("720p", "")
    try:
        no1080p = no720p.replace("-1080p", "")
    except:
        no1080p = no720p.replace("1080p", "")
    try:
        nov1x = no1080p.replace("-v1x", "")
    except:
        nov1x = no1080p.replace("v1x", "")
    noHyphens = nov1x.replace("-", " ")
    noUnderscores = noHyphens.replace("_", " ")
    noBracket1 = noUnderscores.replace(")", "")
    noBracket2 = noBracket1.replace("(", "")
    Video0Clean = noBracket2.replace("video0", possiblename)
    Video1Clean = Video0Clean.replace("video1", possiblename)
    Video2Clean = Video1Clean.replace("video2", possiblename)
    Video3Clean = Video2Clean.replace("video3", possiblename)
    Video4Clean = Video3Clean.replace("video4", possiblename)
    MaxresdefaultClean = Video4Clean.replace("maxresdefault", possiblename)
    splittedArray = MaxresdefaultClean.split()
    for part in splittedArray:
        filenamearray.append(part.capitalize())
    print(possiblename)
    os.rename(x, filename.join(filenamearray))
    filenamearray = []
