# Raspberry Pi Face Recognition Security

## Project Description

This project utilizes Raspberry Pi and a camera module to perform **face recognition** for intruder detection. The system will:
- Recognize and authorize known faces
- Detect unauthorized faces and trigger an alert
- Send email notifications with the image of the unauthorized person
- Detect suspicious activity (e.g., lingering in front of the camera)

The project uses **OpenCV** for face recognition, **Python's smtplib** for email alerts, and a **Raspberry Pi** for executing the script.

---

## Dependencies

libraries and tools required:

- **Python 3.x**
- **OpenCV**: For face recognition and image processing.
- **smtplib**: For sending email alerts.
- **imghdr**: For handling image formats.
- **Numpy**: For numerical operations.

