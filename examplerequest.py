# create an exmample request to the server using sc.png

import requests
import base64
import io
from PIL import Image

c = requests.post('http://localhost:5000/upload', files={'image': open('example.png', 'rb')}).text

print(c)