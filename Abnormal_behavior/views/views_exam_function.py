from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from ..models import User_Management, Exam_Management
from django.utils import timezone

# Create your views here.
def create_new_room(request):
    if request.method == "POST":
        exam_id = request.POST.get('exam_id')
        course_id = request.POST.get('course_id')
        exam_date = request.POST.get('exam_date')
        duration = request.POST.get('duration')
        room_id = request.POST.get('room_id')
        supervisor = request.POST.get('supervisor') 
        
        # Add any other fields you need
        if Exam_Management.objects.filter(exam_id=exam_id).exists():
            messages.error(request, "Exam Id already exists")
            return redirect(create_new_room)
        if Exam_Management.objects.filter(room_id=room_id, exam_date=exam_date).exists():
            messages.error(request, "An exam with the same room and date already exists")
            return redirect(create_new_room)
        else:
            # Create new room
            new_room = Exam_Management(
                exam_id=exam_id,
                course_id=course_id,
                exam_date=exam_date,
                duration=duration,
                room_id=room_id, 
                supervisor=User_Management.objects.get(username=supervisor),  
            )
            new_room.save()
            messages.success(request, "Your room has been created successfully")
            return render(request, "Exam_room/excel2json.html", {'exam_id': exam_id, 'course_id': course_id})
    return redirect('home')


def access_room(request):
    if request.method == "POST":
        exam_id = request.POST.get("exam_id")
        exam_code = request.POST.get("exam_code")
        try:
            exam = Exam_Management.objects.get(exam_id=exam_id)
        # print(exam_code)
        # print(exam.supervisor.ucode)
        except:
            return render(request, 'Error/404.html')
        current_time = timezone.now()
        status = 'available'
        request.session['in_exam'] = True
        if exam.exam_date < current_time:
            status = "overdue"
            
        if exam_code == exam.supervisor.ucode:
            
            request.session['access'] = True
            json_files = Quiz.objects.filter(exam_id=exam_id).values_list('json_data', flat=True)
            context = {
                'exam_id': exam_id,
                'duration': exam.duration,
                'exam_date': exam.exam_date,
                'supervisor_name': exam.supervisor.username,
                'status': status,
                'number_question': len(json_files[0])
            } 
            # exam_room(request, exam_id)
            return render(request, "Exam_room/exam_menu.html", context)
            # Redirect the user to the exam_room view with the exam_id parameter
            # return redirect(reverse('exam_room', kwargs={'exam_id': exam_id}))
        else:
            request.session['in_exam'] = False
            return redirect('home')
    
    return render(request, "Error/404.html")

def exam_room(request, exam_id):
    # Check if the user is allowed to access the exam
    if not request.session.get('in_exam', False):
        # Redirect to a different page if the user is not in an exam
        return redirect('home') 
    # Fetch json_data from Quiz objects related to the exam
    json_files = Quiz.objects.filter(exam_id=exam_id).values_list('json_data', flat=True)
    
    context = {
        'exam_id': exam_id,
        'json_data': json_files, # Convert QuerySet to list
        'number_question': len(json_files[0]),
    } 
    
    return render(request, 'Exam_room/exam_room1.html', context)

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Abnormal_behavior.models import Quiz
import json

@csrf_exempt
def quiz(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            exam_id = data.get('exam_id')
            course_id = data.get('course_id')
            json_data = data.get('json_data')

            # Save JSON data to Quiz model
            quiz = Quiz.objects.create(
                exam_id=exam_id,
                course_id=course_id,
                json_data=json_data
            )

            return JsonResponse({'message': 'JSON data saved successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


