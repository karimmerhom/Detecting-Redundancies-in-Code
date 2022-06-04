from difflib import SequenceMatcher
import multiprocessing as mp
from multiprocessing import Process, Value, Queue
import datetime as dt

def similar(a,b):
    return SequenceMatcher(None,a,b).ratio()

string1 = "public static void pause @NonNull AppCompatActivity activity if instance null return instance isResumed false if instance subs null instance subs clear if instance backgroundSubscriptions null instance backgroundSubscriptions clear if activity isFinishing instance backgroundSubscriberViews remove activity getClass getName if instance context null instance context getClass getName equals activity getClass getName instance context null"
string2 = "public static void pause @NonNull AppCompatActivity activity if instance null return instance isResumed false if instance subs null instance subs clear if instance backgroundSubscriptions null instance backgroundSubscriptions clear if activity isFinishing instance backgroundSubscriberViews remove activity getClass getName if instance context null instance context getClass getName equals activity getClass getName instance context null"

with open('allMethods') as f:
              lines1 = f.readlines()
              finalResults = open("finalResults",'a')
              x = 0 
              while(x < len(lines1)): 
                 print(x+1)
                 method =lines1[x].split()
                 tag = method[0]+" "+method[1]
                 method.pop(0)
                 method.pop(0)
                 listToStr = ' '.join([str(elem) for elem in method])
                 z = 0 
                 while( z < len(lines1) ):
                  methodCompare =lines1[z].split()
                  tagCompare = methodCompare[0]+" "+methodCompare[1]
                  methodCompare.pop(0)
                  methodCompare.pop(0)
                  listToStrCompare = ' '.join([str(elem) for elem in methodCompare])
                  if(x!=z):
                   if (similar(listToStr, listToStrCompare)>0.8):
                      finalResults.writelines(str(x+1))
                      finalResults.writelines("---->")
                      finalResults.writelines(str(z+1))
                      finalResults.writelines("---->")
                      finalResults.writelines(str(similar(listToStr, listToStrCompare)))
                      finalResults.writelines("\n")
                  z+=1
                 x+=1