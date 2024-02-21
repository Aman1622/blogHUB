from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class myblog(models.Model):
    blog_name=models.CharField(max_length=20)
    description = models.TextField()
    content=models.TextField()
    image=models.ImageField(upload_to='blog_images/')
    

    def __str__(self):
        return self.blog_name

class myrating(models.Model):
    blog=models.ForeignKey(myblog,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    rating=models.IntegerField(default=1)
    class Meta:
        unique_together=(('blog','user'))
    def __str__(self):
        return str(self.rating)+f'--{self.user.username}--'