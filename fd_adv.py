import cv2
# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


def get_torso(path,img_name, ext):
    

    if ext in ['jpg', 'jpeg', 'png']:
        try:
            # Read the input image
            img = cv2.imread(f'{path}/{img_name}.{ext}')
        except Exception as e:
            print("yooo")
            print(f"Error': {e}")
            return None

        # Convert into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # Create faces list for face data
        torso = []
        for (x, y, w, h) in faces:
            bw = (7/3)*w
            semi_bw = bw/2
            p_y = y+h + int(0.5*h)
            final_y = p_y + int(3*h)
            torso_topleft = [int((x+(w/2)) - semi_bw) , p_y]
            torso_bottomright = [int((x+(w/2)) + semi_bw), final_y]
            torso.append([torso_topleft, torso_bottomright])
        return torso


if __name__ == "__main__":
    print(get_torso('images', '8', 'jpg'))