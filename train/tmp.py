import os
import cv2
import xmltodict
import sys
import json
import random



def toTxt(path, outDir, txtName, all = False):
	
	f = open(txtName, 'a+')
	file_list = []
	for root, dirs, files in os.walk(path):
		for name in files:
			if name.endswith('png'):
				file_list.append(os.path.join(root, name))
	if os.path.isfile(path):
		file_list.append(path)
	
	for img in set(file_list):
		name = img
		img = cv2.imread(img)
		
		if not all:
			if img.mean() > 80:
				
				f.write( name + '\n')
		else:
			f.write( name + '\n')




if __name__ == "__main__":

	path = 'neg'
	outDir = 'neg'
	txtName = 'xx.txt'

	toTxt(path, outDir, txtName)
	toTxt('all_neg', outDir, txtName, True)
	

	
	