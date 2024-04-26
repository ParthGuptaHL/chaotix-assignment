from django.db import models

class GeneratedImage(models.Model):
    """
    Model to store prompt and path of generated image
    """
    
    text_prompt = models.CharField(max_length=255)
    image_url = models.URLField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Generated Image: {self.text_prompt}"
