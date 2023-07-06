import requests

API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
headers = {"Authorization": "Bearer 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"}


speech = input("Enter The Text: \n")

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response

output = query({
    "inputs": speech,
})


if output.status_code == 200:
    output_filename = "output.wav"  # Specify the desired filename with the appropriate extension
    with open(output_filename, "wb") as f:
        f.write(output.content)
    print(f"Output saved as {output_filename}")
else:
    print("Error occurred during the API request.")

