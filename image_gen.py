from openai import OpenAI
import requests
import os
from urllib.parse import urlparse
from image_processing import create_input_image

client = OpenAI()

def download_image(url):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    print('downloading image ...') 
    response = requests.get(url)
    save_path = os.path.join('results', filename)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Image downloaded successfully as '{filename}'")
    else:
        print("Failed to download image")

def generate_image(prompt):
    response = client.images.generate(
        model="dall-e-2",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    response_json = response.to_json()
    print(response_json)
    download_image(response.data[0].url)

def edit_image(prompt, input_image):
    response = client.images.edit(
        image=open(input_image, "rb"),
        prompt=prompt,
        n=2,
        size="1024x1024"
    )
    response_json = response.to_json()
    print(response_json)
    for img_data in response.data:
        download_image(img_data.url)


if __name__ == "__main__":
    # generate_image("Hyper-realistic image of a superhero standing heroically, with his full face clearly visible, looking directly towards the camera, with long flowing hair cascading down their back. The superhero wears a majestic, billowing cape that extends gracefully behind them. Their pose exudes confidence and strength. The background is plain white.")
    # generate_image("Hyper-realistic image of a super villain standing in a serious pose, with his full face clearly visible, looking directly towards the camera. The villain is a scientist. Their pose exudes dominance and menace. The background is plain white.")
    # create_input_image('results/persona1.png', 'results/persona2.png')
    edit_image("Profile pictures of a superhero on the top left and a super villain below that. Rest of the scene depicts both the characters intensely looking at each other prepared for a fight. The background depicts a destoryed part of the city.", os.path.join("results", "input-image.png"))
