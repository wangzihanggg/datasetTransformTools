import cv2
def video():
    videoCapture = cv2.VideoCapture('./infantry_dark.MOV')
    fps = 30           # 保存视频的帧率,可改变
    size = (1280, 720)  # 保存视频大小

    videoWriter = cv2.VideoWriter('./infantry_dark_720p.MOV',
                                 cv2.VideoWriter_fourcc('X','V','I','D'), fps, size)
 
    while True:
        success, frame = videoCapture.read()
        if success:
            img = cv2.resize(frame, size)
            videoWriter.write(img)
        else:
            print('break')
            break
 
    #释放对象，不然可能无法在外部打开
    videoWriter.release()
 
 
if __name__ == '__main__':
    video()
    print("end!")
