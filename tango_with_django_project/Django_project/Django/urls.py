from django.urls import path
from Django import views

app_name = 'django'

urlpatterns = [
    path('', views.index, name = 'index'),
]