import cv2
import numpy as np
import os

def load_video(path_of_video):
    if not os.path.exists(path_of_video):
        print(f"Video not found \n {path_of_video}")
        return None
    video=cv2.VideoCapture(path_of_video)
    cv2.namedWindow("Video")
    cv2.createTrackbar("ksize","Video",3,100,lambda x:None)
    #how to create trackbar?
    while True:
        status,frame=video.read()
        height,width,_=frame.shape
        #print(f'height: {height}, width:{width}')
        if not status:
            print("Video could not be read")
            break
        #operations
        #1.resize
        frame=cv2.resize(frame,(None,None),fx=.5,fy=.5) #half the size None None means no size 
        #2.convert to grayscale?
        #frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        #3.blur
        ksize=cv2.getTrackbarPos("ksize","Video")
        try:frame=cv2.GaussianBlur(frame,(ksize,ksize),0)
        except:pass

        frame=cv2.GaussianBlur(frame,(5,5),0) #gausiam blur , highlight,blur,sharpen etc all are mathematical functions 
        #4.add text
        frame= cv2.putText(
            frame,
            "Stone paper scissor",
            (width//2-500,height//2-150), #coordinates/origin
            cv2.FONT_HERSHEY_SIMPLEX,#font face
            1,#font size/scale
            (0,0,255),#red
            2#thickness
        )
        #5.add graphics
        cv2.imshow("Video",frame)
        if cv2.waitKey(10)==ord('q'):#1 represents 1 millisecond
            break
        #clear the memory 
    video.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    videofile=r"C:/Users/dell/Pictures/Camera Roll/stone_paper_scissor.mp4"
    load_video(videofile)
    #cross doesnt work with imshow()