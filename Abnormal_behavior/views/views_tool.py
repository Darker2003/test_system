from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from ..models import User_Management, History_Management, Exam_Management, Exam_Room_Doing, Bill, IP_state
from ..forms import ImageUploadForm
import os
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_datetime
from datetime import datetime
from django.contrib.auth.decorators import user_passes_test

@csrf_exempt  # Only for demonstration purposes. Consider a more secure approach for production.
def write_token(request):
    if request.method == 'POST':
        try:
            # Get the erd_id from the POST data
            erd_id = request.POST.get('erd_id', None)

            if erd_id is not None:
                # Write the erd_id to the file
                with open('token.txt', 'a') as file:
                    file.write(erd_id + '\n')

                return HttpResponse("Token written successfully.")
            else:
                return HttpResponse("Error: erd_id not provided in the POST data.")
        except Exception as e:
            return HttpResponse(f"Error writing token: {e}")
    else:
        return HttpResponse("Invalid request method. Only POST is allowed.")

def upload_img(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Process the uploaded file here
            # For example, saving it to the database or file system

            # Return a custom response
            return HttpResponse('Thank you for uploading the image!')
    else:
        form = ImageUploadForm()

    return render(request, 'Exam_room/upload_img.html', {'form': form})

@csrf_exempt
def tool_login_sdkjbaiuwq983y912u32186hsjzbguhcvwehui873y89n8y7s(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        client_ip = request.META.get('REMOTE_ADDR')

        # Log the information (you can replace this with your desired logging mechanism)
        print("Client IP:", client_ip, "Username:", username)
        try:
            user = User_Management.objects.get(username = username)
            if user.upassword == password:
                request.session['user'] = username
                return HttpResponse('0')
        except:
            return HttpResponse('1')
    return render(request, "Error/404.html")

@csrf_exempt
def exam_login_sjdby18h27ndwn7y127t3672wcdawd1jdfkk009saidjw8890jwhau(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        exam_id = request.POST.get('exam_id')
        exam_code = request.POST.get('exam_code')
        client_ip = request.META.get('REMOTE_ADDR')
        print(f'Username: {username}, exam_id: {exam_id}, client_ip: {client_ip}')
        try:
            user = User_Management.objects.get(username = username)
            if user.upassword == password:
                try:
                    exam = Exam_Management.objects.get(exam_id = exam_id)
                    if exam.supervisor.ucode == exam_code:
                        erd_id = Exam_Room_Doing.objects.get(exam_id = exam_id, username = username)
                        erd_id = erd_id.erd_id
                        request.session['erd_id'] = erd_id
                        return HttpResponse(f'{erd_id}')
                    else:
                        return HttpResponse('False')
                except:
                    return HttpResponse('False')
        except:
            return HttpResponse('False')
    return render(request, "Error/404.html")

def check_state_jaghfuie19sba872t1dnx1y278yn7tx176bn27txb67n1xg7rfxbd5(request):
    if request.method == 'GET':
        input_string = request.GET.get('inf', f'a%a')  # Default to 'a' if 'inf' is not provided
        check_status = input_string.split('%')
        current_time = datetime.now()
        current_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
        his_count = History_Management.objects.count()
        client_ip = request.META.get('REMOTE_ADDR')
        print(f'Client IP Address: {client_ip}, Time: {current_time}, INFO: {check_status}')
        
        if check_status[2] == 'check':
            if check_status[1] == 'False':
                History_Management.objects.create(his_id=f'h{his_count+1}', erd_id=Exam_Room_Doing.objects.get(erd_id=f'{check_status[0]}'), htime=parse_datetime(f'{current_time}'), labels='normal')
            elif check_status[1] == 'True':
                History_Management.objects.create(his_id=f'h{his_count+1}', erd_id=Exam_Room_Doing.objects.get(erd_id=f'{check_status[0]}'), htime=parse_datetime(f'{current_time}'), labels='abnormal')
            
            IP_state.objects.create(IP=client_ip, erd_id=Exam_Room_Doing.objects.get(erd_id=f'{check_status[0]}'), time=parse_datetime(f'{current_time}'), state='online')
            
            return HttpResponse('0')

        if check_status[2] == 'unlock':
            erd_his = History_Management.objects.filter(erd_id=f'{check_status[0]}').order_by('-htime').first()
            text = erd_his.state
            return HttpResponse(text)
    return render(request, "Error/404.html")

def unlock_jiuhduigaiugyueihdg19y7e61hdtg76badr56n816nb2t5c7ecne8t72nd(request):
    if request.method == 'GET' and 'access' in request.session:
        erd_his = History_Management.objects.filter(his_id=request.GET.get('his_id'), erd_id = request.GET.get('erd_id')).first()
        erd_his.state = '1'
        erd_his.save()
        return HttpResponse('Ok')
    return render(request, "Error/404.html")

# Custom function to check if the user is a superuser
def is_superuser(user):
    return user.is_authenticated and user.is_superuser

# Apply the user_passes_test decorator to the view
@user_passes_test(is_superuser, login_url='/admin/login/')
def dash_index(request):
    bill_count = Bill.objects.count()
    vip_user = User_Management.objects.filter(utype = 'vip').count()
    total_room = Exam_Management.objects.count()
    total_abnormal = History_Management.objects.filter(labels = 'abnormal').count()
    context = {
        'first_name': request.user.first_name,
        'bill_count': bill_count,
        'vip_user': vip_user,
        'total_room': total_room,
        'total_abnormal':  total_abnormal,
    }
    return render(request, 'Dashboard_admin/index.html', context)
