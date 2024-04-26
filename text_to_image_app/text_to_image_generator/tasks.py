from celery import shared_task
from text_to_image_generator.stability_ai_post import text_to_image

@shared_task
def generate_image(text):
    """
    Task for calling Stability AI API
    """
    
    image = text_to_image(text)
    return image