from django import http
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
from detectme.admin import UserEntryAdmin
 
from detectme.camera import VideoCamera_py  
from detectme.models import UserEntry

from django.core.paginator import Paginator
 
##########################################
def show_all_page(request):
    context={}
    filtered_quiz= UserEntry.objects.all()
    paginator = Paginator(filtered_quiz, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['object_list'] = page_obj
    return render(request, "list_questions.html", context)

##########################################

def list_questions(request):
    queryset=UserEntry.objects.all()
    filter_query=UserEntry.objects.all()[:5]
    if filter_query.count() < 2:
        print('Looks ok  !')
    else:
        print('somehting wrong !')
        context={"object_list":filter_query}
    return render(request,"list_questions.html",context)

####################################
def home(request):
    context = {}
    return render(request, "base.html", context)

def cv2_page(request):
    return render(request, "open_cv.html" )

def auto_record(request):
    return render(request, "auto_record.html" )

####################################


def gen(camera):
    
	while True:
		frame = camera.get_frame()
        
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

 
#Method for phone camera
def webcam_feed(request):
    
	return StreamingHttpResponse(gen(VideoCamera_py()),
                    #video type
					content_type='multipart/x-mixed-replace; boundary=frame')

