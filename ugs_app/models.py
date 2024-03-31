from django.db import models
from django.db.models.deletion import RESTRICT,CASCADE
from django.contrib.auth.models import User,AbstractUser
import uuid
import datetime
from django.utils.translation import gettext as _





class UserAccount(models.Model):
    user=models.OneToOneField(User, on_delete=CASCADE)
    contact_no=models.IntegerField(null=True, blank=True)
    usertype=models.CharField(max_length=50, choices=[('SUPER ADMIN','SUPER ADMIN'),('ADMIN','ADMIN'),('DECLARATOR','DECLARATOR'),('LOADER','LOADER'),('AGENT','AGENT'),('PLAYER','PLAYER')]) 
    referral_code=models.CharField(max_length=100,null=True, blank=True)
    user_agent=models.ForeignKey(User,on_delete=CASCADE,related_name='user_agent')
    status=models.CharField(max_length=50,default='ACTIVE',choices=[('ACTIVE','ACTIVE'),('INACTIVE','INACTIVE'),('BANNED','BANNED')])
    
    def __str__(self):
        return self.user.username
    

class UserWallet(models.Model):
    user=models.OneToOneField(User, on_delete=CASCADE,default=1,related_name='user')
    w_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    w_balance=models.IntegerField(null=True, blank=True)
    w_points=models.IntegerField(null=True, blank=True)
    w_commission=models.IntegerField(null=True, blank=True)
    w_status=models.CharField(max_length=50,choices=[('ACTIVE','ACTIVE'),('INACTIVE','INACTIVE'),('BANNED','BANNED')])
    w_dateupdate=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.username +' - '+str(self.w_id))
    

class Games(models.Model):
    g_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    g_name=models.CharField(max_length=50, blank=True)
    g_desc=models.CharField(max_length=100, blank=True)
    g_link=models.CharField(max_length=100, blank=True)
    g_image=models.ImageField(blank=True)

    def __str__(self):
        return str(self.g_name )