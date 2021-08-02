from flask import Flask, request
from flask_cors import CORS
from utils import b64_img, img_b64
import cv2


app = Flask(__name__)
CORS(app)

@app.route('/greyscale', methods= ['POST'])
def main():
    request_payload = request.get_json()
    img = b64_img(request_payload['data'])
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    greybase = img_b64(grayscale)
    response = {'data': greybase}
    return response

@app.route('/binarythreshold/<thrshval>', methods= ['POST'])
def ma(thrshval):
    request_payload = request.get_json()
    img = b64_img(request_payload['data'])
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(grayscale,int(thrshval),255,cv2.THRESH_BINARY)
    base = img_b64(thresh1)
    response = {'data': base}
    return response

@app.route('/binarythresholdinv/<thrshval>', methods= ['POST'])
def mas(thrshval):
    request_payload = request.get_json()
    img = b64_img(request_payload['data'])
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(grayscale,int(thrshval),255,cv2.THRESH_BINARY_INV)
    base = img_b64(thresh1)
    response = {'data': base}
    return response

@app.route('/gaussinablur/<kernelsize>', methods= ['POST'])
def m(kernelsize):
    request_payload = request.get_json()
    img = b64_img(request_payload['data'])
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grayscale,(int(kernelsize),int(kernelsize)),0)
    base = img_b64(blur)
    response = {'data': base}
    return response

@app.route('/canny/<min>/<max>', methods= ['POST'])
def s(min, max):
    request_payload = request.get_json()
    img = b64_img(request_payload['data'])
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(grayscale,int(min),int(max))
    base = img_b64(edges)
    response = {'data': base}
    return response


@app.route('/down', methods= ['POST'])
def sd():
    request_payload = request.get_json()
    img = b64_img(request_payload['data'])
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    lower_reso = cv2.pyrDown(grayscale)
    base = img_b64(lower_reso)
    response = {'data': base}
    return response

@app.route('/up', methods= ['POST'])
def sdd():
    request_payload = request.get_json()
    img = b64_img(request_payload['data'])
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    upper = cv2.pyrUp(grayscale)
    base = img_b64(upper)
    response = {'data': base}
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug= True)



