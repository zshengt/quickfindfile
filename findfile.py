#! usr/bin/python
#coding=utf-8 

import os

class FindFile(object):
    def __init__(self):
        pass
    def search(self, str, dir):
        for x in os.listdir(dir): 
            path = os.path.join(os.path.abspath(dir), x)
            if os.path.isdir(path):
                self.search(str, path)
            if os.path.isfile(path) and str in x:
                print path

f = FindFile()
while True:
    print "into"
    string = raw_input()
    if(string == "q"):
        print "have exit"
        break
    else:
        f.search(string, "F:\mdbqw")
