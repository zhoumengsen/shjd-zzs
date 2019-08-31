#!/usr/bin/python
# encoding: utf-8
import os

print "请确认当前项目路径："
os.system("pwd")

isY = raw_input("(y/n)")
if isY != "y" :
	exit()

csvPath = raw_input("请填写csv绝对路径：")

gitUrl = 'git clone ssh://mengsen.zhou@116.62.41.107:29418/';
fileObject = open(csvPath,"r")

content = fileObject.read()
	

lineList = content.split('\n')

for line in lineList[1:] :
	if line.strip()=='':
		print "存在空行-clone结束"
		break
	
	stringList = line.split(',')
	print stringList
	url = gitUrl + stringList[4] + ".git" 
	result = os.system(url)
	if result != 0:
	 		print line[0] + "-clone失败"
	 		break

fileObject.close()
 
print "clone over"
