from PIL import Image
import base64
import io
import cv2
import numpy as np


def b64_img(base64img):
    base64_decoded = base64.b64decode(base64img)
    image = Image.open(io.BytesIO(base64_decoded))
    image_np = np.array(image)
    return image_np


def img_b64(img):
    cv2.imwrite('./test.jpg', img)
    
    with open('./test.jpg', "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read())
        b64 = encoded_image.decode('utf-8')
    return b64

if __name__ == "__main__":
    img = cv2.imread('/home/mugesh/r/demo/Assets/img2.jpeg')
    b  =  img_b64(img)
    ig = b64_img(b)
    cv2.imshow("Frame", ig) 
    cv2.waitKey(0)

