from django.shortcuts import render, redirect
from ..models import User_Management, History_Management, Exam_Management
from datetime import datetime

#python manage.py runsslserver --cert abnormal_certificate.crt --key abnormal.key 0.0.0.0:443

# Create your views here.
def home(request):
#Use for home page
    #Calculate number of user
    user_count = User_Management.objects.count()
    
    current_time = datetime.now()
    #Fileter ended exam
    ended_exams = Exam_Management.objects.filter(exam_date__lt=current_time)
    ended_exams = ended_exams.count()
    
    # Filter history entries where labels is 'abnormal'
    abnormal_history_entries = History_Management.objects.filter(labels='abnormal')
    abnormal_history_entries = abnormal_history_entries.count()
    
#Use for accessroom
    try:
        del request.session['access']
    except:
        return render(request, 'Interface/index.html', {'user_count': user_count, 'ended_exams': ended_exams, 'abnormal': abnormal_history_entries})
    return render(request, 'Interface/index.html', {'user_count': user_count, 'ended_exams': ended_exams, 'abnormal': abnormal_history_entries})

def course(request):
    if 'user_name' in request.session:
        # User is logged in, render the course page
        return render(request, 'Interface/course.html')
    else:
        # User is not logged in, redirect to login page
        return redirect('login')

def about(request):
    return render(request, "Interface/about.html")

def price(request):
    return render(request, "Interface/price.html")

def feature(request):
    return render(request, "Interface/feature.html")

def team(request):
    return render(request, "Interface/team.html")

def testimonial(request):
    return render(request, "Interface/testimonial.html")

def quote(request):
    return render(request, "Interface/quote.html")

def contact(request):
    return render(request, "Interface/contact.html")
