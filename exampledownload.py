import requests
import base64
import io
from PIL import Image

 
 
# example request to server using code ujenit

c = requests.post('http://localhost:5000/download', data='ujenit').content

# convert the bytes to an image
img = Image.open(io.BytesIO(c))
# save to test folder

img.save('test.png')