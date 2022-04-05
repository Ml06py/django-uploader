from django.db import models
from account.models import User
from datetime import date
# Create your models here.
class UserFile(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True,blank=True,null=True)
    owner =  models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    file = models.FileField(upload_to="uploads/files")
    expiration = models.DateField(blank=True,null=True)
    def __str__(self):
        return self.title
