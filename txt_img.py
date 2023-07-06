import requests

API_URL = "https://api-inference.huggingface.co/models/stablediffusionapi/anything-midjourney"
headers = {"Authorization": "Bearer api_org_MOxxxxxxxxxxxxxxxxxxxxxxxxRX"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": "a man in desert",
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))



image.save("a.jpg")
