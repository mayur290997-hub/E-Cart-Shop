from django.urls import path
from store import views

app_name='store'

urlpatterns = [
    path('index',views.index,name="index"),
]