import cv2
import mediapipe as mp
<<<<<<< HEAD
mp_face_detection = mp.solutions.face_detection  #to detect
mp_drawing = mp.solutions.drawing_utils #to draw
 
#created by google in 2023 only under construction
# copied from Legacy section from overview from mediapipe page 

def detect_faces(cam_idx=0,model=0,cnf=.5):
    #
# For webcam input:
    cap = cv2.VideoCapture(cam_idx)
    #code hoisting andr ki requirement k bhar nikalna jisse use ki ja ske , eg bhar se value dena andar declare krne k bajae
    with mp_face_detection.FaceDetection(
        model_selection=model, 
        min_detection_confidence=cnf) as face_detection: #confidence= the accuracy jisse wo keh skta ki jo detect kia wo sahi h , amount of guess 50% ki sahi h  jb tk 50% na lge sb tk mt bole ears nose 
=======
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

def detect_faces(cam_idx=0, model=0, cnf=.5):
    cap = cv2.VideoCapture(cam_idx)
    with mp_face_detection.FaceDetection(
        model_selection=model,
        min_detection_confidence=cnf
    ) as face_detection:
>>>>>>> 85a4da63c9b54f19ef7418dfd9f7f6b558dbdde6
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
<<<<<<< HEAD
                # If loading a video, use 'break' instead of 'continue'.
                continue

            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = face_detection.process(image)

            # Draw the face detection annotations on the image.
=======
                continue
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = face_detection.process(image)
>>>>>>> 85a4da63c9b54f19ef7418dfd9f7f6b558dbdde6
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            if results.detections:
                for detection in results.detections:
                    mp_drawing.draw_detection(image, detection)
<<<<<<< HEAD
                # Flip the image horizontally for a selfie-view display.
            cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
            if cv2.waitKey(5) & 0xFF == 27:
                break
        cap.release()   
        cv2.destroyAllWindows()    
if __name__=="__main__":
    detect_faces(model=1)
    #if model =  0 detects till 2meter 
    #if model=1 detects 5 meter
=======
            cv2.imshow('Face Detection', cv2.flip(image, 1))
            if cv2.waitKey(5) & 0xFF == 27:
                break
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_faces(model=1)
>>>>>>> 85a4da63c9b54f19ef7418dfd9f7f6b558dbdde6
