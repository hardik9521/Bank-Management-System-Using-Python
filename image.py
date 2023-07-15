import cv2
class Image:
    def capture_image(self,accnumber):
        capture = cv2.VideoCapture(0)

        if not capture.isOpened():
            print("failed to open webcam")
            capture_image(accnumber)
        
        ret,frame = capture.read()
        if not ret:
            print("Failed to capture")
            capture.release()
            capture_image(accnumber)
        
        cv2.imwrite(f"{accnumber}.jpg",frame)
        capture.release()


    
    
    
