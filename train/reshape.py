import os
import cv2
import xmltodict
import sys
import json
import random



POS_PATH = 'raw_pos'
NEG_PATH = 'raw_neg'
POS_OUT, POS_TXT = 'pos', 'pos.txt'
NEG_OUT, NEG_TXT = 'neg', 'neg.txt'

xx,cnt = 0, 0

def xml2dict(xml_path):
    xml_file = open(xml_path, 'r')
    xml_str = xml_file.read()
    json = xmltodict.parse(xml_str)
    return json


def toTxt(path, outDir, outName, txtName, isPos = True, xmin = 0, ymin = 0, xmax = 0, ymax = 0, isRandom = False, VAR = 0, MEAN = 0):
	'''
		path: 需要遍历的文件夹或者文件
		outDir:	reshape后的文件地址
		outName : reshape后的文件名
		txtName: txt文件地址
		isPos:	是否是正样例
	'''
	f = open(txtName, 'a+')
	new_size = (36, 55)

	file_list = []
	for root, dirs, files in os.walk(path):
		for name in files:
			file_list.append(os.path.join(root, name))
	if os.path.isfile(path):
		file_list.append(path)
	
	for img in set(file_list):
		img = cv2.imread(img)
		bg_img = False
		choose = []
		img_resize = None
		if isPos:
			img_resize = cv2.resize(img[xmin:xmax, ymin:ymax], new_size, interpolation = cv2.INTER_CUBIC)
		else:
			multiple = 1.3
			if not isRandom:
				# 选择其他亮度周边图像
				tmpImg = img.copy()
				tmpImg[xmin:xmax, ymin:ymax] = img.mean()
				lo, hi = 0, 255
				mi = (lo+hi)//2
				P = 0.03*img.shape[0]*img.shape[1]

				while lo+1 < hi:
					tmp = (tmpImg>mi).sum()
					if  tmp > P:
						lo = mi
					elif tmp < P:
						hi = mi
					else:
						break
					mi = (lo+hi)//2
				# print ('mi', mi)
				for i in range(img.shape[0]):
					for j in range(img.shape[1]):
						if img[i,j].mean() >= mi:
							check_size = 2
							if i-check_size>=0 and i+check_size<=255 and j-check_size>=0 and j+check_size<=255:
								if img[i-check_size:i+check_size, j-check_size:j+check_size].mean() >= mi:
									try:
										x_1, y_1 = max(i-int(new_size[1]*multiple)//2, xmin), max(j-int(new_size[0]*multiple)//2, ymin)
										x_2, y_2 = min(i+int(new_size[1]*multiple)//2, xmax), min(j+int(new_size[0]*multiple)//2, ymax)
										# 判断相交性
										if x_2 > x_1 and y_2 > y_1:
											if (x_2-x_1)*(y_2-y_1) / new_size[0]*new_size[1] > 0.5:
												continue
										# 去掉与选择像素较近的点
										ok = True
										for point in choose:
											if abs(point[0]-i) < 10 and abs(point[1]-j) < 10:
												ok = False
										if ok:
											choose.append([i,j])
											# print ('xx', img[i-check_size:i+check_size, j-check_size:j+check_size].mean())
											# print ('xxx', img[i-int(new_size[1]*multiple)//2:i+int(new_size[1]*multiple), j-int(new_size[0]*multiple)//2:j+int(new_size[0]*multiple)//2].mean())
									except:
										pass
			else:
				# 随机选择背景图片
				time = 0
				while time < 20:
					x = random.randint(0, 512 - int(new_size[1]*multiple))
					y = random.randint(0, 512 - int(new_size[0]*multiple))
					maybe_img = img[x:x+int(new_size[1]*multiple), y:y+int(new_size[0]*multiple)]

					N = new_size[0]*new_size[1]
					sum1 = maybe_img.sum()
					mean = sum1/N
					sum2 = ((maybe_img - mean)**2).sum()
					var = sum2/(N*N)

					time += 1
					if var > VAR and mean > MEAN:
						x_1, y_1 = max(x, xmin), max(y, ymin)
						x_2, y_2 = min(x+int(new_size[1]*multiple), xmax), min(y+int(new_size[0]*multiple), ymax)

						# 判断相交性
						if x_2 > x_1 and y_2 > y_1:
							if (x_2-x_1)*(y_2-y_1) / new_size[0]*new_size[1] > 0.5:
								continue
						bg_img = True
						img_resize = maybe_img
						break
			
		if not isPos and not bg_img and isRandom:
			continue
		if not isPos and not isRandom and len(choose)==0:
			continue

		save_img = []
		if not isPos and not isRandom:
			print (len(choose))
			for point in choose:
				i , j= point[0], point[1]
				img_resize = img[i-int(new_size[1]*multiple)//2:i+int(new_size[1]*multiple)//2, j-int(new_size[0]*multiple)//2:j+int(new_size[0]*multiple)//2]
				save_img.append(img_resize)
				# print (img_resize.mean(), i, j)
		else:
			save_img.append(img_resize)

		for index,img_resize in enumerate(save_img):
			img_gray = cv2.cvtColor(img_resize,cv2.COLOR_RGB2GRAY)
			tmp_name = outName[:-4] + str(index) + '.png'
			cv2.imwrite( outDir + '/' + tmp_name,img_gray)
			if isPos:
				f.write(outDir + '/' + tmp_name +' 1 0 0 36 55\n')
			else:
				f.write( outDir + '/' + tmp_name + '\n')





if __name__ == "__main__":

	xmlPath = '/Users/hqw/Desktop/computer_vision/标注/xml'

	for root, dirs, files in os.walk(xmlPath):
		for name in files:
			fileName = os.path.join(root, name)
			# print (fileName)
			if not fileName.endswith('xml'):
				continue
			text = xml2dict(fileName)
			path = text['annotation']['path']
			filename = text['annotation']['filename']
			xmin = int(text['annotation']['object']['bndbox']['xmin'])
			xmax = int(text['annotation']['object']['bndbox']['xmax'])
			ymin = int(text['annotation']['object']['bndbox']['ymin'])
			ymax = int(text['annotation']['object']['bndbox']['ymax'])

			# toTxt(path, POS_OUT, filename, POS_TXT, True, ymin, xmin, ymax, xmax)

			for i in range(6):
				var = (i>0)*5
				mean = 30*(i+1)
				isRandom = (i<5)
				toTxt(path, NEG_OUT, filename[:-4]+ "_" +str(i) + ".png", NEG_TXT, False, ymin, xmin, ymax, xmax, isRandom, var, mean)

	