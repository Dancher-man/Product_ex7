from django.contrib.auth.views import LoginView
from django.urls import path

app_name = 'source'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),

]