#!/usr/bin/python
# Combines two scripture.py list files into one
# JP Tomkins (jtomkins@icr.org)
# Uses new builtin set() method in python v2.6
# Set module deprecated in python v2.6

# Copy the two files needed to the ~/bin/wrd_pkg/comblist directory
# Makes backup of original "~/bin/wrd_pkg/scriptures.py" file
import shutil
shutil.copy ("/Users/jtomkins/bin/wrd_pkg/scriptures.py","/Users/jtomkins/bin/wrd_pkg/scriptures.py-bak")
shutil.copy ("/Users/jtomkins/bin/wrd_pkg/scriptures.py-bak","/Users/jtomkins/bin/wrd_pkg/comblist/scriptures1.py")
shutil.copy ("/Users/jtomkins/ppc_ho/scriptures.py","/Users/jtomkins/bin/wrd_pkg/comblist/scriptures2.py")


# Modify copied files - rename list variables
import fileinput

for line in fileinput.FileInput("scriptures1.py",inplace=1):
	line=line.replace("scripturelist = [","list1 = [")
	print line

for line in fileinput.FileInput("scriptures2.py",inplace=1):
	line=line.replace("scripturelist = [","list2 = [")
	print line

# Combining lists, removing duplicates, printing new list file
from scriptures1 import list1
from scriptures2 import list2
from heapq import merge

combined_list1 = list(merge(list1, list2))

combined_list2 = set(combined_list1)

scripturelist = open("scriptures_new.py", "w")

scripturelist.write("scripturelist = [\n")

scripturelist.close()

scripturelist = open("scriptures_new.py", "a")

for item in sorted(combined_list2):
	scripturelist.write("\"")
	scripturelist.write(item)
	scripturelist.write("\",\n")

scripturelist.write("]")
scripturelist.close()

# Removes last comma in list - needs help
for line in fileinput.FileInput("scriptures_new.py",inplace=1):
	line=line.replace("\",\n]","\n]")
	print line

# Copy new file to functional location "~/bin/wrd_pkg/scripturelist.py"

shutil.copy ("/Users/jtomkins/bin/wrd_pkg/comblist/scriptures_new.py","/Users/jtomkins/bin/wrd_pkg/scriptures.py")