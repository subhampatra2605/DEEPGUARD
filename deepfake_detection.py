# import cv2
# import numpy as np
# from keras.models import load_model

# def detect_deepfake(file):
#     # Load the trained model
#     model_path = r'E:\deepfake_detection_app\deepfake\25_3.h5'
#     model = load_model(model_path)

#     # Read the file
#     img = cv2.imdecode(np.fromstring(file.read(), np.uint8), cv2.IMREAD_UNCHANGED)
    
#     # Preprocess the image
#     resized_img = cv2.resize(img, (224, 224))
#     input_img = resized_img / 255.0
#     input_img = np.expand_dims(input_img, axis=0)
    
#     # Perform prediction
#     predictions = model.predict(input_img)
    
#     # Determine result
#     result = "FAKE" if predictions >= 0.3 else "REAL"
    
#     return result
