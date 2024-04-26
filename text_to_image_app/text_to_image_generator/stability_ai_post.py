import base64
import os
import uuid

import requests
from dotenv import load_dotenv

from .models import GeneratedImage

load_dotenv()

engine_id = "stable-diffusion-v1-6"
api_host = os.getenv('API_HOST', 'https://api.stability.ai')
api_key = os.getenv('STABILITY_API_KEY')

def text_to_image(text_prompt):
    """
    API call to post text prompts and get image in response
    """
    
    if api_key is None:
        raise Exception("Missing Stability API key.")

    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "text_prompts": [
                {
                    "text": text_prompt
                }
            ],
            "cfg_scale": 7,
            "height": 1024,
            "width": 1024,
            "samples": 1,
            "steps": 30,
        },
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    #Saving the generated image in file system and DB
    for i, image in enumerate(data["artifacts"]):
        image_data = base64.b64decode(image["base64"])
        image_name = str(uuid.uuid4()) + ".png"
        image_url = f"images/{image_name}"
        generated_image = GeneratedImage.objects.create(text_prompt=text_prompt, image_url=image_url)
        generated_image.save()

        with open(f"images/{image_name}", "wb") as f:
            f.write(image_data)
