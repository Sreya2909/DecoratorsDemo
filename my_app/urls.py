from django.urls import path 

from . import views 

 

urlpatterns = [ 

    path('dashboard/', views.dashboard, name='dashboard'), 

    path('add-user/', views.add_user, name='add_user'), 

    path('contact/', views.contact, name='contact'), 

    path('static-content/', views.static_content, name='static_content'), 

] 