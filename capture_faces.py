import cv2
import os

# Create the directory to save images if it doesn't exist
if not os.path.exists("known_faces"):
    os.makedirs("known_faces")

# Initialize the face recognizer
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize webcam
cap = cv2.VideoCapture(0)

# Get the name of the person for whom we want to capture faces
name = input("Enter the name of the authorized person: ")

# Initialize counter for image numbers
image_count = 0

# Start capturing faces
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        image_count += 1
        # Save the captured image in the known_faces folder
        face_image = frame[y:y+h, x:x+w]
        cv2.imwrite(f"known_faces/{name}_{image_count}.jpg", face_image)
        
        # Draw rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('Capturing Faces', frame)
    
    # Break the loop after capturing 50 faces or press 'q' to quit
    if image_count >= 50:
        break
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

print(f"{image_count} images of {name} have been captured.")
