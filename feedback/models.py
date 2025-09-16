from django.db import models

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.name if self.name else 'Anonymous'} on {self.created_at.strftime('%Y-%m-%d %H:%M')}"
