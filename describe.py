from ollama import chat
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

image_path = "id_fr.png"

messages = [
    {
        'role': 'user',
        'content': "AS OCR take the data and convert it to text as json format",
        'images': [encode_image(image_path)]
    },
]

stream = chat(
    model='llava',
    messages=messages,
    stream=True,
)

with open("result.txt", "w") as output_file:
    for chunk in stream:
        output_file.write(chunk['message']['content'])