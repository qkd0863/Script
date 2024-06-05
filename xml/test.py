from PIL import Image
from io import BytesIO
import requests

# 테스트용 이미지 URL
url = 'https://www.example.com/path/to/image.jpg'
response = requests.get(url)

if response.status_code == 200:
    image = Image.open(BytesIO(response.content))
    image.show()
else:
    print("Failed to retrieve the image")