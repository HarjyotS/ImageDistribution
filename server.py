# create a flask server that can get images from the client and save them in the images folder with a unique code and return the code to the client, and also get the code from the client and return the image to the client

from flask import Flask, request, send_file
from flask_cors import CORS
import os
import random
import string
import base64
import io
from PIL import Image

app = Flask(__name__)
CORS(app)

# create a folder to store the images
if not os.path.exists('images'):
    os.makedirs('images')
    

# function to generate a random string of length 6
def randomString(stringLength=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


@app.route('/upload', methods=['POST'])
def upload():
         # get the image from the request
    img = request.files['image']

    # get the random string
    rand = randomString()
    
    # save the image
    img.save('images/' + rand + '.png')

    # return the random string
    return rand

@app.route('/download', methods=['POST'])
def download():
    # get the random string from the request
    rand = request.data.decode('utf-8')

    # open the image
    img = Image.open('images/' + rand + '.png')

    # convert the image to bytes
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()

    # return the image
    return send_file(io.BytesIO(img_bytes), mimetype='image/png')

@app.route('/download/<string:rand>', methods=['GET'])
def download2(rand):
    
    # open the image
    img = Image.open('images/' + rand + '.png')

    # convert the image to bytes
    img_bytes = io.BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes = img_bytes.getvalue()

    # return the image
    return send_file(io.BytesIO(img_bytes), mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)