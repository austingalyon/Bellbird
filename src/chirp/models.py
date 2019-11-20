from django.db import models

# Create your models here.
class Chirp(models.Model):
  text = models.CharField(max_length=140)
  upvotes = models.IntegerField(default=0)
  created_at = models.TimeField(auto_now_add=True)

  def upvote(self):
    upvotes = self.upvotes + 1
    
    return