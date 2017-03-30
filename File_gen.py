#!/usr/bin/python
import os
import sys

numFiles = 10
fileFolder = "test_files"
prefix = "file"

def main():
	makeDir(fileFolder)

	#makes blank files
	num = 1
	while num <= numFiles:
		filename = prefix + "%d" % num
		fileLocation = fileFolder + "/" + filename
		f = open(fileLocation,"w+")
		f.close
		num += 1

#makes directory for test files
def makeDir(path):
	cwd = os.getcwd()
	directory = cwd + "/" + path
	if not os.path.exists(directory):
		os.mkdir(directory)
	#cleans directory if it already exists
	else:
		files = os.listdir(directory)
		for file in files:
			fileLocation = directory + "/" + file
			os.remove(fileLocation)

if __name__ == '__main__':
	main()