import os
import sys
import shutil

DirList = []
TargetPath = "C:/Users/PC/Desktop"
indice = len(TargetPath) + 1

try:
    open("D:/")

except:
    sys.exit

def DirCopy(Path):
    # print(Path)
    for item in os.scandir(Path):
            
            # print(item.name)

            if item.is_dir():
                # print("it's a dir")
                try:
                    os.mkdir("D:/" + Path[indice:] + "/" + item.name)
                except: pass
                DirCopy(Path + "/" + item.name)
            else:
                # print("copy to D:/" + Path[indice:])
                shutil.copy(Path + "/" + item.name,"D:/" + Path[indice:])
                

for item in os.scandir(TargetPath):
    #  print(item.name,"1")
     if item.is_dir():
          try:
            os.mkdir("D:/" + item.name)
          except: pass
          DirList.append(TargetPath+"/"+item.name)

for dir in DirList:
     DirCopy(dir)