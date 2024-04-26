from django.http import HttpResponse
from .tasks import generate_image
from celery import Celery

# text prompts to be sent to stability ai api
text_prompts = ["A red flying dog", "A husky ninja", "A footballer kid", "A wizard on Mars", "Baby Dragon"]

def generate_images(request):
    """
    API endpoint to trigger parallel image generation
    """
    
    app = Celery('text_to_image_app')
    app.config_from_object('django.conf:settings', namespace='CELERY')
    app.task(generate_image)

    # Iterate over text prompts and call the Celery task for each prompt
    for text_prompt in text_prompts:
        generate_image.delay(text_prompt)

    return HttpResponse(f"Triggered {len(text_prompts)} parallel calls. Results available soon.")
