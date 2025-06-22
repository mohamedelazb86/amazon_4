from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code



ROLE_STATUS=[
    ('Manager','Manager'),
    ('Employee','Employee'),
    
]
class Profile(models.Model):
    user=models.OneToOneField(User,related_name='profile_user',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='photo_user')
    code=models.CharField(max_length=75,default=generate_code)
    phone=models.CharField(max_length=25,null=True,blank=True)
    role=models.CharField(max_length=120,choices=ROLE_STATUS)

    def __str__(self):
        return str(self.user)
