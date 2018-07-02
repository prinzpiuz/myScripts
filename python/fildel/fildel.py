#*****************************fildel***********************************
#............................v0.0.1....................................
#this is a script to delete files in directory 
#having fileSize greater than given size as parameter
#scripted by prizpiuz
#for bugs & queries <prinzpiuz@disroot.org> 
import sys
import os
import itertools
from os import listdir
from os.path import isfile, join
#function to show how to use the script
def usage():
	print("fildel v0.0.1")
	print("funBy_prinzpiuz_")
	print("usage:filedel <sizeInMb>")
#list all the files with size in bytes
#convert 2d list to 1d
#convert 1d list to dictionary using itertools
def listFiles(cwd):
	onlyfiles = [f for f in listdir(cwd) if isfile(join(cwd, f))]
	for i in range(len(onlyfiles)):
	   onlyfiles[i] = [onlyfiles[i], os.path.getsize(onlyfiles[i]) >> 20]
	onlyfiles = sum(onlyfiles,[])    
#	print(onlyfiles)
	d = dict(itertools.zip_longest(*[iter(onlyfiles)] * 2, fillvalue="")) 
	return d 	
#delete files in current working directory
def fildel(f,arg):
	for key in f:
		if f[key] > arg:
			os.remove(key)


if __name__=='__main__':
	if len(sys.argv) < 2:
		usage()	
	else:
		cwd=os.getcwd()
		print("working directory:%s " %cwd)
		f=listFiles(cwd)
		print(f)
		arg=int(sys.argv[1])
		fildel(f,arg)
#to show contents in folder after deletions		
		cur=listFiles(cwd)
		print(cur)

		
		
			
