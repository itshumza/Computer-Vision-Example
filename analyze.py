from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from config import Credentials
endpoint = Credentials['END_POINT']
subscription_key = Credentials['API_KEY']
# Create an authenticated client
credentials = CognitiveServicesCredentials(subscription_key)
client = ComputerVisionClient(endpoint, credentials)
# Read and process the image
image_path = '1.jpg'
image_data = open(image_path, "rb")
result = client.analyze_image_in_stream(image_data, ['Description', 'Tags', 'Adult', 'Objects', 'Faces'])
print(result)