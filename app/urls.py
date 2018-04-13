from django.conf.urls import url
from app import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^post/', views.post, name='post'),

]
