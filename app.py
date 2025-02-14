# import cv2

# # Load the pre-trained face detection model
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # Initialize the video capture
# cap = cv2.VideoCapture(0)  # Use 0 for your primary webcam, 1 for secondary, and so on

# while True:
#     # Read a frame from the video capture
#     ret, frame = cap.read()

#     # Convert the frame to grayscale (face detection works on grayscale images)
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect faces in the grayscale frame
#     faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#     # Draw rectangles around the detected faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

#     # Display the resulting frame
#     cv2.imshow('Face Detection', frame)

#     # Check for the 'q' key to exit the loop
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the video capture object and close all windows
# cap.release()
# cv2.destroyAllWindows()

# # from flask import Flask, render_template, Response
# # import cv2

# # app = Flask(__name__)

# # face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# # cap = cv2.VideoCapture(0)

# # def detect_faces():
# #     while True:
# #         ret, frame = cap.read()
# #         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# #         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
# #         for (x, y, w, h) in faces:
# #             cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
# #         ret, jpeg = cv2.imencode('.jpg', frame)
# #         yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + jpeg.tobytes() + b'\r\n')

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # @app.route('/video_feed')
# # def video_feed():
# #     return Response(detect_faces(), mimetype='multipart/x-mixed-replace; boundary=frame')

# # if __name__ == '__main__':
# #     app.run(debug=True)

