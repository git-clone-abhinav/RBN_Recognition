import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
img = cv2.imread('images/4.png')

# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Draw rectangle around the faces
for (x, y, w, h) in faces:
    bw = (7/3)*w
    semi_bw = bw/2
    p_y = y+h + int(0.5*h)
    final_y = p_y + int(3*h)
    cv2.rectangle(img, ( int((x+(w/2)) - semi_bw) , p_y), (int((x+(w/2)) + semi_bw), final_y), (0,255,255), 2)
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output
cv2.imshow('img', img)
cv2.waitKey()