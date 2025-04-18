import cv2
import numpy as np
import paho.mqtt.client as mqtt
import time

# MQTT Setup
mqtt_broker = "mqtt.eclipse.org"  # Replace with your broker's IP if using a local broker
mqtt_port = 1883
mqtt_topic = "home/intruder_alert"
mqtt_client = mqtt.Client("IntruderAlertClient")

# Initialize face recognition
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the authorized faces (for simplicity, using two images here)
authorized_faces = ["person1.jpg", "person2.jpg"]

def send_mqtt_alert(unauthorized_face_image):
    # Publish a message to the MQTT broker
    mqtt_client.connect(mqtt_broker, mqtt_port, 60)
    message = f"Unauthorized person detected! Image: {unauthorized_face_image}"
    mqtt_client.publish(mqtt_topic, message)
    print("MQTT message sent!")

# Set up video capture (camera)
cap = cv2.VideoCapture(0)

# Loop to capture frames
while True:
    ret, frame = cap.read()
    
    # Convert to grayscale (required for face detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    
    for (x, y, w, h) in faces:
        # Draw rectangle around the face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Crop the detected face
        face_roi = frame[y:y+h, x:x+w]
        
        # Here, you would add face recognition code (e.g., compare face_roi with the authorized_faces)
        # For simplicity, we'll assume unauthorized faces are detected by default
        is_authorized = False  # Set to True if a recognized face is detected
        
        if not is_authorized:
            # Save the unauthorized face image
            unauthorized_face_image = "unauthorized_face.jpg"
            cv2.imwrite(unauthorized_face_image, face_roi)
            
            # Send MQTT alert
            send_mqtt_alert(unauthorized_face_image)
    
    # Display the video feed
    cv2.imshow('Face Recognition', frame)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
