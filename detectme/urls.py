from django.conf.urls import url, include
from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name="home"),
    path('cv2_page', views.cv2_page, name="cv2-page"),
    path('auto_record', views.auto_record, name="auto_record"),
    path('webcam_feed', views.webcam_feed, name='webcam_feed'),
    path('', views.show_all_page, name='list_questions'),
    
    ]