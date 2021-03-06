from django.db import models
from django.urls import reverse
# Create your models here.

class Post(models.Model):
  """The blog Post."""
  title = models.CharField(max_length=200)
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  body = models.TextField()

  def __str__(self):
    """Unicode representation of Post."""
    return self.title

  def get_absolute_url(self):
    return reverse('blog:post_detail', args=[str(self.id)])
