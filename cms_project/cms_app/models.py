from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Other relevant fields

# You can similarly define the User model if you need additional fields
