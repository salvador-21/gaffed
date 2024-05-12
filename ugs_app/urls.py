from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('getuser',views.getuser,name='getuser'),
    path('', views.index, name='index'),
    path('homepage', views.homepage, name='homepage'),
    path('user_account', views.user_account, name='user_account'),
    path('adminAccReg',views.adminAccReg,name='adminAccReg'),
    path('auth_user',views.auth_user,name='auth_user'),
    path('signout',views.signout,name='signout'),
    path('ad/games',views.admin_games,name='admin_games'),
    path('ad/add_games',views.add_games,name='add_games'),
    path('betting',views.betting,name='betting'),

]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)