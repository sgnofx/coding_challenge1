from django.urls import path
from authenticator import views

app_name = 'authenticator'
urlpatterns = [
    path('login/', views.login, name = 'login'),
]