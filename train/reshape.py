import os
import cv2

POS_PATH = 'raw_pos'
NEG_PATH = 'raw_neg'
POS_OUT, POS_TXT = 'pos', 'pos.txt'
NEG_OUT, NEG_TXT = 'neg', 'neg.txt'

def toTxt(path, outDir, txtName, isPos = True):

	cnt = 0
	f = open(txtName, 'w')
	new_size = (50, 80)
	for root, dirs, files in os.walk(path):
		for name in files:
			# print(os.path.join(root, name))
			img = cv2.imread(os.path.join(root, name))
			if isPos:
				img_resize = cv2.resize(img, new_size, interpolation = cv2.INTER_CUBIC)
			else:
				if img.shape[0] >= new_size[0] and img.shape[1] >= new_size[1]:
					img_resize = img
				else:
					newH = img.shape[0] if img.shape[0] > new_size[0] else new_size[0]
					newW = img.shape[1] if img.shape[1] > new_size[1] else new_size[1]
					img_resize = cv2.resize(img, (newH, newW), interpolation = cv2.INTER_CUBIC)

			img_gray = cv2.cvtColor(img_resize,cv2.COLOR_RGB2GRAY)
			
			cv2.imwrite( outDir + '/' + name + '_reshape_.jpg',img_gray)
			if isPos:
				f.write((cnt > 0)* '\n' + outDir + '/' + name + '_reshape_.jpg 1 0 0 50 80')
			else:
				f.write((cnt > 0)* '\n' + outDir + '/' + name + '_reshape_.jpg\n')
			cnt += 1
	print ('tot imgs %d' % cnt)

if __name__ == "__main__":

	toTxt(POS_PATH, POS_OUT, POS_TXT)

	toTxt(NEG_PATH, NEG_OUT, NEG_TXT, False)