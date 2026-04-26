import cv2
import numpy as np
from mss import mss
import time

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
print("Switch to YouTube! Starting in...")
for i in range(3, 0, -1):
    print(f"{i}...")
    time.sleep(1)
with mss() as sct:
    entire_screen = np.array(sct.grab(sct.monitors[1]))
    entire_screen = cv2.cvtColor(entire_screen, cv2.COLOR_BGRA2BGR)
    roi = cv2.selectROI("Select Video Area", entire_screen, False)
    cv2.destroyWindow("Select Video Area")
    monitor = {"top": int(roi[1]), "left": int(roi[0]), "width": int(roi[2]), "height": int(roi[3])}
    while True:
        frame_raw = np.array(sct.grab(monitor))
        frame = cv2.cvtColor(frame_raw, cv2.COLOR_BGRA2BGR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(50, 50))
        face_gallery = []
        for (x, y, w, h) in faces:
            face_img = frame[y:y+h, x:x+w]
            if face_img.size > 0:
                face_resized = cv2.resize(face_img, (200, 200))
                face_gallery.append(face_resized)
            if len(face_gallery) >= 5:
                break
        if len(face_gallery) > 0:
            combined_display = np.hstack(face_gallery)
            cv2.imshow("Normalized Gallery", combined_display)
        else:
            placeholder = np.zeros((200, 200, 3), dtype=np.uint8)
            cv2.putText(placeholder, "Searching...", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            cv2.imshow("Normalized Gallery", placeholder)
        cv2.moveWindow("Normalized Gallery", 0, 0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cv2.destroyAllWindows()