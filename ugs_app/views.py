from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,AbstractUser
from django.contrib.auth.admin import UserAdmin
from django.contrib import messages
from django.utils import timezone
from .models import UserAccount,UserWallet,Games
import datetime,time
from django.db.models import Q
from django.utils.crypto import get_random_string
from .forms import SignUpForm,LoginForm,UserForm,WalletForm,GameForm
from django.core import serializers
# from django.contrib.sites.models import Site
# from django_minify_html.middleware import MinifyHtmlMiddleware


# class ProjectMinifyHtmlMiddleware(MinifyHtmlMiddleware):
#     minify_args = MinifyHtmlMiddleware.minify_args | {
#         "keep_comments": True,
#     }
# Create your views here.

# def referral(request):
#     print(request.GET.get('agent'))
#     return redirect('registration')
# @login_required(login_url='signin')
@csrf_exempt
def auth_user(request):
     form = LoginForm(request.POST or None)
     msg=''
     
     if request.method == 'POST':
          if form.is_valid():
               username=form.cleaned_data.get('username')
               password=form.cleaned_data.get('password')
               user=authenticate(username=username, password=password)
               if user is not None:
                    msg='login'
                    login(request,user)
                    status=1
               else:
                    status=0
                    msg='err'
          else:
              status=0
              msg='err'

     return JsonResponse({'data':msg})

def signout(request):
    logout(request)
    return redirect('/')

def index(request):
     if request.user.is_authenticated:
          return redirect('homepage')
     referral=request.META['HTTP_HOST']+'/agent='+get_random_string(50)
     context={
          'game_frm':GameForm()
     }
     return render(request,'ugs_app/auth/signin.html',context)

@login_required(login_url='/')
def homepage(request):
     referral=request.META['HTTP_HOST']+'/agent='+get_random_string(50)
     getuser=UserAccount.objects.all().select_related('user')
     context={
           'page':'Dashboard'
     }
     return render(request,'ugs_app/homepage/index.html',context)
@login_required(login_url='/')
def user_account(request):
     referral=request.META['HTTP_HOST']+'/agent='+get_random_string(50)
     getuser=UserAccount.objects.all().select_related('user')
     getwallet=UserWallet.objects.all().select_related('user')
     context={
          'page':'User Account',
          'users':getuser,
          'wallet':getwallet,
          'wallet_frm':WalletForm(),
          'signup_frm':SignUpForm(),
          'user_frm':UserForm(),
     }
     return render(request,'ugs_app/homepage/user_account.html',context)

@csrf_exempt
def adminAccReg(request):
    referral=get_random_string(100)
#     getu=UserAccount.objects.select_related('user').get(referral_code='PAyNdxN0Q4UBS1uVvsHxLkfi40NdUfI1UTpmZEKfVtLOrHUUG1')
#     refby=int(getu.id)
#     print(request.user.id)

    form=SignUpForm()
    userform=UserForm()
    walletform=WalletForm()
    if request.method=='POST':
       account = SignUpForm(data=request.POST)
       userinfo = UserForm(data = request.POST)
     #   wallet=WalletForm(data=request.POST)
      
       if account.is_valid() and userinfo.is_valid() :
            user = account.save()
            user.set_password(user.password)
            user.save()
            info = userinfo.save(commit = False)
            info.user = user
            info.usertype=request.POST.get('usertype')
            info.referral_code=referral
            info.user_agent=request.user
            info.status='ACTIVE'
            info.save()
            wall=walletform.save(commit = False)
            wall.user=user
            wall.w_balance=0
            wall.w_points=0
            wall.w_commission=0
            wall.w_status='ACTIVE'
            wall.save()
            data='ok'
           
       else:
            data='Error Validating'
    else:
          data=request

    return JsonResponse({'data':data})


############################ LOAD USER

@csrf_exempt
def getuser(request):
     userg=UserAccount.objects.select_related('user','user_agent').all().order_by('-user_id', '-id')
     userw=UserWallet.objects.select_related('user').all().order_by('-user_id')
    
     user_data = [
        {      
             'u_id':item.user.id,
            'username': item.user.username,
             'usertype': item.usertype,
            'status': item.status,
            'join_date':item.user.date_joined
          #   'balance': item.user_wallet.w_balance
            # Add more fields as needed
        }
        for item in userg
     ]
     wallet_data=[
          {
               'w_user':item.user.id,
               'w_balance':item.w_balance,
          }
          for item in userw
     ]
     return JsonResponse({'data':user_data,'wdata':wallet_data},safe=False)


def admin_games(request):
    page='Games'
    return render(request,'ugs_app/homepage/admin_games.html',{'title':'Homepage','page':page})

@csrf_exempt
def add_games(request):
     for filename, file in request.FILES.items():
      print(filename, file)
      data=file
     return JsonResponse({'data':str(data)})