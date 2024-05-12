from django.db import models
from django.db.models.deletion import RESTRICT,CASCADE
from django.contrib.auth.models import User,AbstractUser
import uuid
import datetime
from django.utils.translation import gettext as _





class UserAccount(models.Model):
    user=models.OneToOneField(User, on_delete=CASCADE)
    contact_no=models.CharField(max_length=11,null=True, blank='00000000000')
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
    g_category=models.CharField(null=True,max_length=50,choices=[('E-SABONG','E-SABONG'),('BALL GAMES','BALL GAMES')])
    g_link=models.CharField(max_length=100, blank=True)
    g_image=models.ImageField(blank=True, null=True ,upload_to='uploads/')
    g_by=models.IntegerField(blank=True,null=True)

    def __str__(self):
        return str(self.g_name )


class Fight(models.Model):
    f_id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    f_number=models.IntegerField(blank=True,null=True)
    f_game=models.ForeignKey(Games,on_delete=CASCADE,related_name='f_game')
    f_wala_odd=models.IntegerField(blank=True,null=True)
    f_meron_odd=models.IntegerField(blank=True,null=True)
    f_walatotalbet=models.IntegerField(blank=True,null=True)
    f_merontotalbet=models.IntegerField(blank=True,null=True)
    f_winner=models.CharField(max_length=100, blank=True)
    f_status=models.CharField(null=True,max_length=50,choices=[('OPEN','OPEN'),('CLOSED','CLOSE'),('DONE','DONE')])
    f_update=models.DateTimeField(auto_now=True)
    f_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(str(self.f_game) +' ( Fight #: '+str(self.f_number)+' )' )