from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials 
captions = []
tags = []
endpoint = "https://tutorquest.cognitiveservices.azure.com/"
subscription_key = "00db62b481ce4b6487cb94e298fde02d"
# Create an authenticated client
credentials = CognitiveServicesCredentials(subscription_key)
client = ComputerVisionClient(endpoint, credentials)
# Read and process the image
image_path = '4.jpg'
image_data = open(image_path, "rb")
result = client.analyze_image_in_stream(image_data, ['Description', 'Tags', 'Adult', 'Objects', 'Faces'])
for caption in result.description.captions:
    #st.text(caption.text)
    captions.append(caption.text)
    for tag in result.description.tags:
        tags.append(tag)

print(tags)
print(captions)