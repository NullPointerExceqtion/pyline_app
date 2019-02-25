from django.urls import path
from . import views
 
urlpatterns = [
    path('<int:id>', views.hello_template, name='hello_template'),
]