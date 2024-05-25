import threading
import cv2
from deepface import DeepFace

face_match=False

def check_face(frame,reference_img):
   global face_match
   try:
      if DeepFace.verify(frame, reference_img)['verified']:
         face_match = True
      else:
         face_match=False
   except ValueError:
      face_match = False

def driver_face_recognition(resident_id):
   global face_match
   cap = cv2.VideoCapture(0)

   cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
   cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

   counter = 0
   path="E:/se_project/.venv/"+str(resident_id)+ ".jpg"
   print(path)
   reference_img = cv2.imread(path)
   # print(reference_img)

   while True:
      ret, frame = cap.read()

      if ret:
         if counter % 30 == 0:
            try:
               threading.Thread(target=check_face(frame,reference_img)).start()
            except ValueError:
               # print("No Face Detected!")
               pass
         counter += 1

         if face_match:
            cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
         else:
            cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

         cv2.imshow("video", frame)
         # print(frame)

      key = cv2.waitKey(1)
      if key == ord("q"):
         return face_match
   cv2.destroyAllWindows()

