import cv2
import numpy as np
import os
<<<<<<< HEAD

def load_video(path_of_video):
    if not os.path.exists(path_of_video):
        print(f"Video not found \n {path_of_video}")
        return None
    video=cv2.VideoCapture(path_of_video)
    while True:
        status,frame=video.read()
        if not status:
            print("Video could not be read")
            break
        cv2.imshow("Video",frame)
        if cv2.waitKey(100)==ord('q'):#1 represents 1 millisecond
            break
        #clear the memory 
    video.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    videofile=r"C:/Users/dell/Pictures/Camera Roll/WIN_20231106_14_42_38_Pro.mp4"
    load_video(videofile)
    #cross doesnt work with imshow()
=======
def load_video(path_of_video):
    if not os.path.exists(path_of_video):
        print(f"🤯 Video file not found\n{path_of_video}")
        return None 
    video = cv2.VideoCapture(path_of_video)
    while True:
        status , frame = video.read()
        if not status:
            print("🤯 Video could not be read!!")
            break
        cv2.imshow("Video",frame)
        if cv2.waitKey(10) == ord('q'): # 1 represents 1 millisecond
            break
    # clear the memory
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    videofile = r"C:\Users\ZAID\Videos\the lost legacy\lost_legacy.mp4"
    load_video(videofile)
>>>>>>> 85a4da63c9b54f19ef7418dfd9f7f6b558dbdde6
