import os

findCount = 0
findId = "QString"
findDir = "/Users/wangnz/Documents/mydev/replace"

resultFile = os.path.join(findDir,"result.txt")


def writeResultAndPrint(fullPath):
	print (fullPath)
	file = open(resultFile,'a')
	file.write(fullPath)
	file.write("\n")
	file.close()


def findKey(fullPath):
	file = open(fullPath,'r')/Users/wangnz/Documents/mydev/python/project1/test2.py
	content = file.read()/Users/wangnz/Documents/mydev/python/project1/test2.py
	file.close()

	isExist = content.find(findId)
	if isExist > 0:
		global findCount
		findCount = findCount + 1
		writeResultAndPrint(fullPath)



def findFiles():
	for dirPath,dirNames,fileNames in os.walk(findDir):
		for file in fileNames:
			fullPath = os.path.join(dirPath,file)
			print(fullPath)
#			findKey(fullPath)


#	print("找到了字符串个数=" + str(findCount))

def clean():
	if os.path.exists(resultFile):
		os.remove(resultFile)

findFiles()