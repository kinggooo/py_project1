import os
import re

findCount = 0
findId = "QString"
findDir = "/Users/wangnz/Downloads"
resultFile = os.path.join(findDir,"result.txt")
src_file_path = '/Users/wangnz/Downloads/04150930.html'
dst_file_path = '/Users/wangnz/Downloads/04151334.html'

def findNotExistsLine(src_file,dst_file):
	s_file = open(src_file,'r')
	d_file = open(dst_file,'r')
	d_content = d_file.read()
	pattern = re.compile(r'.*(<A.*)')
	for line in s_file:
		m = pattern.match(line)
		if m <> None:
			row = m.group(1)
			isExist = d_content.find(row)
			if isExist == -1:
				print(row)
	s_file.close()

findNotExistsLine(src_file_path,dst_file_path)