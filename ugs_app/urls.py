from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage', views.homepage, name='homepage'),
    path('user_account', views.user_account, name='user_account'),
    path('adminAccReg',views.adminAccReg,name='adminAccReg'),
    path('getuser',views.getuser,name='getuser'),
    path('auth_user',views.auth_user,name='auth_user'),
    path('signout',views.signout,name='signout'),
    path('ad/games',views.admin_games,name='admin_games'),
    path('ad/add_games',views.add_games,name='add_games'),

]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)