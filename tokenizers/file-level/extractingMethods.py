import logging
import multiprocessing as mp
from multiprocessing import Process, Value, Queue
import re
import os
import platform
import collections
import tarfile
import sys
import hashlib
import datetime as dt
import zipfile
import javalang

File_allMethods = open("allMethods",'a')

with open('allTokens') as f:
    lines1 = f.readlines()

with open('blocks.file') as f:
    lines2 = f.readlines()

j = 0
methods_list = []
while(j < len(lines1)): 
  firstFIle = lines1[j]
  arrayFirstFile = firstFIle.split()
  j +=1
  i = 0 
  while (i < len(arrayFirstFile)-3):
  
    if (arrayFirstFile[i] == 'public' or  arrayFirstFile[i] == 'protected' or arrayFirstFile[i] == 'private') :
             s = ""
             s =  str(arrayFirstFile[len(arrayFirstFile)-2]) + " " + str(arrayFirstFile[len(arrayFirstFile)-1])
             s+= " "
             s+= arrayFirstFile[i]
             i+=1
             flag = True
             while ((i < len(arrayFirstFile)-3) and flag == True):
                  if (arrayFirstFile[i] == 'public' or  arrayFirstFile[i] == 'protected' or arrayFirstFile[i] == 'private') :
                            flag = False 
                  else:
                      s+= " "
                      s += arrayFirstFile[i]
                      i+=1      
                    
             File_allMethods.writelines(s)
             File_allMethods.writelines('\n')
             methods_list.append(s)
    else:
        i+=1
print(methods_list)