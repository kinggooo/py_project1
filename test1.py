#!/usr/bin/env python
#coding:utf8

import re

findCount = 0
findId = "QString"
findDir = "/Users/wangnz/Downloads"
# resultFile = os.path.join(findDir,"result.txt")
source_path = './20210531.html'
target_path = './20210601.html'


def findNotExistsLine(src_file,dst_file):
	s_file = open(source_path,'r')
	t_file = open(target_path,'r')
	t_content = t_file.read()
	pattern = re.compile(r'.*(<A.*A>)')
	for s_line in s_file:
		m = pattern.match(s_line)
		if m <> None:
			href = m.group(1)
			isExist = t_content.find(href)
			if isExist == -1:
				print(href)
	s_file.close()

findNotExistsLine(source_path,target_path)
