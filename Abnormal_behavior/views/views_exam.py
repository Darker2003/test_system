from django.shortcuts import render, redirect

#python manage.py runsslserver --cert abnormal_certificate.crt --key abnormal.key 0.0.0.0:443

# Create your views here.
def exam_menu(request):
    if 'access' in request.session:
        # print(request.session['access'])
        return render(request,  'Exam_room/exam_menu.html')
    else:
        return render(request, "Error/404.html")

def finish_exam(request):
    request.session['in_exam'] = False
    # Redirect to a different page after finishing the exam
    return redirect('home')  # Replace 'home' with your home page's URL pattern

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Abnormal_behavior.models import Save_Quiz
import json

@csrf_exempt
def save_quiz(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            exam_id = data.get('exam_id')
            json_data = data.get('json_data')

            # Save JSON data to Quiz model
            quiz = Save_Quiz.objects.create(
                exam_id=exam_id,
                json_data=json_data
            )

            return JsonResponse({'message': 'JSON data saved successfully'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
