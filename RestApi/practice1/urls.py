from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello_world,name='HelloWorld'),
    path('post_student/',views.post_student,name='post_student')
]