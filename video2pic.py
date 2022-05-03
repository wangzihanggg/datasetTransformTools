import cv2
import os
#要提取视频的文件名，隐藏后缀
sourceFileName='star'
#在这里把后缀接上
video_path = os.path.join("carvideo.mp4")
times=0
#提取视频的频率，每１帧提取一个
frameFrequency=14

outPutDirName="./out/"
if not os.path.exists(outPutDirName):
    #如果文件目录不存在则创建目录
    os.makedirs(outPutDirName)
camera = cv2.VideoCapture(video_path)
while True:
    times+=1
    res, image = camera.read()
    if not res:
        print('not res , not image')
        break
    if times%frameFrequency==0:
        cv2.imwrite(outPutDirName + str(times)+'.jpg', image)
        print(outPutDirName + str(times)+'.jpg')
print('图片提取结束')
camera.release()

