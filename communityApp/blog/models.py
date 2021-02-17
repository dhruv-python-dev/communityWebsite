from django.db import models
from ckeditor.fields import RichTextField
import readtime


class User(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    auth_token = models.CharField(max_length=150)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField()
    mobile = models.IntegerField(blank=False)
    password = models.CharField(max_length=50, null=False)
    confirm_password = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.email

class AuthToken(models.Model):
    pass


class Blog(models.Model):
    blog_date_created = models.DateTimeField(auto_now_add=True)
    blog_title = models.CharField(max_length=250)
    blog_content = RichTextField()
    blog_image = models.ImageField(upload_to='media/blog/',null=True)
    blog_likes = models.IntegerField(default=0)
    slug = models.SlugField(max_length=150,default='')
    user = models.ForeignKey(User, related_name='get_blogs',on_delete=models.CASCADE)

    def get_likes(self):
        return self.blog_likes()

    def liked(self):
        self.blog_likes +=1
        return self.blog_likes

    def __str__(self):
        return self.blog_title


class Comment(models.Model):
    date = models.DateTimeField(auto_now_add=False, default=None)
    body = RichTextField()
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, related_name='get_user', on_delete=models.CASCADE, null=True)
    blog = models.ForeignKey(Blog,related_name='get_comments', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.email
   
class post(models.Models):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=120)
    content = models.TextField()

    def get_readtime(self):
        result = readtime.of_text(self.content)
        return result.text 
    
    def __str__(self):
        return self.title    
    

