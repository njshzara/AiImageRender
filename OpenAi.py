import requests

# Set up the API endpoint and your API key
api_endpoint = "https://api.openai.com/v1/images/generations"
api_key = "YOUR_API_KEY"

# Prompt the user for the text description of the image they want to generate
prompt = input("Enter the text description of the image you want to generate: ")

# Set up the API parameters
data = {
  "model": "image-alpha-001",
  "prompt": prompt,
  "num_images": 1,
  "size": "256x256",
  "response_format": "url"
}

# Make the API request
response = requests.post(api_endpoint, json=data, headers={"Authorization": f"Bearer {api_key}"})

# Print the URL of the generated image
print(response.json()["data"][0]["url"])
