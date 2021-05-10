from django.urls import path
from . import views


urlpatterns = [

    path('', views.account, name="account"),
    path('signin/', views.signin, name="signin"),
    path('logout', views.loggingout, name='logout')
]