from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'memoapp'

urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.AddView.as_view(), name='add'),
    path('update/<int:pk>/', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('signin/', auth_views.LoginView.as_view(template_name='memoapp/signin.html'), name='signin'),
    path('signout/', auth_views.LogoutView.as_view(template_name='memoapp/signout.html'), name='signout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
