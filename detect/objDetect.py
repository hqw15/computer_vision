#-*-coding:utf-8-*-
import numpy as np
import cv2
import os

'''https://docs.opencv2.org/3.4.3/d7/d8b/tutorial_py_face_detection.html
'''

CASCADE = cv2.CascadeClassifier(
    os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "cascade.xml"
        )
    )
#"../train/xml/cascade.xml"

def objDetect(img):
    obj = CASCADE.detectMultiScale(img, 1.1, 5, maxSize = (120,120))
    result = []
    for (x,y,width,height) in obj:
        result.append((x,y,x+width,y+height))
    return result

def retObj(img, saveName):
    obj = objDetect(img)
    print (len(obj))
    if obj:
        for (x1,y1,x2,y2) in obj:
        #     if img[x1:x2, y1:y2].mean() > 80:
            cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),thickness=2)
            # cv2.imwrite(saveName[:-4]+'result.png',img[y1:y2, x1:x2])

    cv2.imwrite(saveName,img)


def readImg(imgPath, isIMA = False):
    if not isIMA: 
        img = cv2.imread(imgPath)
        print (img.shape)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        print (gray.max())
        return gray
    else:
        pass




if __name__=='__main__':

    test_path = '../test_png'

    test_path = '/Users/hqw/Desktop/png/normal/61-70female/WEN_CUN_15233/RT_0_PETCT_WHOLEBODY_PUMC_(ADULT)_20120316_142539_343000/AC_CT_0002'

    for root, dirs, files in os.walk(test_path):
        for name in files:
            if name.endswith('png'):
                print(os.path.join(root, name))
                imgName = os.path.join(root, name)
                img = readImg(imgName)
                retObj(img, '../result/'+name)
			
   