from django.db import models

# Create your models here.
class ChatMessage(models.Model):
    user = models.CharField(max_length=50)
    message = models.CharField(max_length=3000)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message