### Cascade Classifier Training

https://docs.opencv.org/3.3.0/dc/d88/tutorial_traincascade.html
https://blog.csdn.net/fuck487/article/details/81567428

#### step.0	训练数据准备
    input:
        raw_pos:原始正样例
        raw_neg:原始负样例
    output:
        pos:正样例转化图片
        neg:负样例转化图片
        pos.txt:正样例输入文件
        neg.txt:负样例输入文件
    
    **Usage**   python3 reshape.py

#### step.1
    ./opencv_createsamples -vec sample -info pos.txt -num 20 -bg neg.txt -w 50 -h 80

#### step.2

    ./opencv_traincascade -data xml -vec pos.vec -bg neg.txt -numPos 100 -numNeg 1000 -numStages 20 -w 50 -h 50 -minHitRate 0.9999 -precalcValBufSize 1024 -maxFalseAlarmRate 0.5 -mode ALL

----
> 必要的两个可执行文件opencv_createsamples、opencv_traincascade在opencv@2里面有（mac），其他版本好像需要自己生成

