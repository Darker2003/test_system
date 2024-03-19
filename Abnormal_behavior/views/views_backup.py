from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
import mysql.connector as sql
from ..models import User_Management, History_Management, Exam_Management, Exam_Room_Doing, Bill, Quotes
from ..forms import ImageUploadForm
from django.utils import timezone
from collections import Counter
import os
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_datetime
from datetime import datetime
from django.contrib.auth.decorators import user_passes_test
import secrets
import string

#python manage.py runsslserver --cert abnormal_certificate.crt --key abnormal.key 0.0.0.0:443

username  = ''
upassword = ''
utype = ''
remainday = ''
ucode = ''
mail = ''
phone = ''

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

def quotes(request):
    if request.method == 'POST':
        qname = request.POST.get('username')
        qmail = request.POST.get('email')
        qphone = request.POST.get('phone')
        qadvise = request.POST.get('selected_service')
        qmessage = request.POST.get('message')

        if qname and qmail and qphone and qadvise and qmessage:
            # Check if a quote with the given email already exists
            existing_quote = Quotes.objects.filter(qmail=qmail).first()
            if existing_quote:
                messages.error(request, "A quote with this email already exists")
                return redirect('home')

            # Create a new object of the Quotes model and save it to the database
            new_quote = Quotes(
                qmail=qmail,
                qname=qname,
                qphone=qphone,
                qadvise=qadvise,
                qmessage=qmessage
            )
            new_quote.save()
            messages.success(request, "Your information has been saved successfully")
            return redirect('home')  # Redirect to the home page after saving
        else:
            messages.error(request, "Please fill in all required fields")
    else:
        messages.error(request, "Invalid request")

    return render(request, "index.html")

def about(request):
    return render(request, "Interface/about.html")

def course(request):
    if 'user_name' in request.session:
        # User is logged in, render the course page
        return render(request, 'Interface/course.html')
    else:
        # User is not logged in, redirect to login page
        return redirect('login')

def exam_room(request):
    return render(request, 'Exam_room/exam_room1.html')

def create_new_room(request):
    if request.method == "POST":
        exam_id = request.POST.get('exam_id')
        course_id = request.POST.get('course_id')
        exam_date = request.POST.get('exam_date')
        duration = request.POST.get('duration')  
        room_id = request.POST.get('room_id')
        supervisor = request.POST.get('supervisor') 
        print('received')
        # Add any other fields you need
        if Exam_Management.objects.filter(exam_id=exam_id).exists():
            messages.error(request, "Exam Id already exists")
            print('Exam Id already exists')
            return redirect(create_new_room)
        if Exam_Management.objects.filter(room_id=room_id, exam_date=exam_date).exists():
            messages.error(request, "An exam with the same room and date already exists")
            print('An exam with the same room and date already exists')
            return redirect(create_new_room)


        else:
            # Create new user
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
            
            context = {
                'exam_id': exam_id,
                'duration': exam.duration,
                'exam_date': exam.exam_date,
                'supervisor_name': exam.supervisor.username,
                'status': status
            } 
            return render(request, "Exam_room/exam_menu.html",context)
        else:
            request.session['in_exam'] = False
            return redirect('home')
            
    return render(request, "Error/404.html")

def exam_menu(request):
    if 'access' in request.session:
        # print(request.session['access'])
        return render(request,  'Exam_room/exam_menu.html')
    else:
        return render(request, "Error/404.html")

def doing_exam_room(request):
    exam_rooms = Exam_Room_Doing.objects.all()
    return render(request, 'Exam_room/doing_exam_room.html', {'exam_rooms': exam_rooms})

def exam_room_doing_list(request):
    data = list(Exam_Room_Doing.objects.values('erd_id', 'username', 'exam_id', 'state'))  # adjust fields as necessary
    return JsonResponse({'data': data})

def list_exam_room_available(request):
    supervisor_username = request.session.get('user_name') 
    
    if Exam_Management.objects.filter(supervisor=supervisor_username).exists():
        data = list(Exam_Management.objects.filter(supervisor = supervisor_username)
                    .order_by('-exam_date')
                    .values('exam_id', 'course_id', 'exam_date', 'duration','room_id','supervisor'))
        return JsonResponse({'data': data})
    else:
        return JsonResponse({'data': []})

def room_management_data(request, examID):
    # print(request.GET)
    exam_id = request.GET.get('exam_id', None)
    supervisor_username = request.session.get('user_name')

    if Exam_Management.objects.filter(supervisor=supervisor_username).exists():
        # Get the list of unique usernames
        unique_usernames = History_Management.objects.filter(
            erd_id__exam_id__supervisor__username=supervisor_username,
            erd_id__exam_id__exam_id=exam_id
        ).values_list('erd_id__username__username', flat=True).distinct()

        # Calculate the count of 'abnormal' label for each unique username
        username_label_counts = Counter(
            History_Management.objects.filter(
                erd_id__exam_id__supervisor__username=supervisor_username,
                erd_id__exam_id__exam_id=exam_id,
                labels='abnormal',
                erd_id__username__username__in=unique_usernames
            ).values_list('erd_id__username__username', flat=True)
        )
        
        # Fetch all records matching the supervisor and exam_id
        query = History_Management.objects.filter(
            erd_id__exam_id__supervisor__username=supervisor_username,
            erd_id__exam_id__exam_id=exam_id
        ).order_by('-htime').values(
            'his_id',
            'htime',
            'labels',
            'erd_id',
            'erd_id__username__username',
            'erd_id__state',
            'erd_id__exam_id__exam_id',
            'erd_id__exam_id__course_id',
            'erd_id__exam_id__exam_date',
            'erd_id__exam_id__duration',
            'erd_id__exam_id__room_id',
            'erd_id__exam_id__supervisor__username',
        )

        # Convert QuerySet to list for manipulation
        query_list = list(query)

        # Use a dictionary to keep only the latest entry for each user
        latest_entries = {}
        for entry in query_list:
            username = entry['erd_id__username__username']
            # If the username is not in the dictionary or if the current entry's time is later, update the dictionary
            if username not in latest_entries or latest_entries[username]['htime'] < entry['htime']:
                latest_entries[username] = entry
                latest_entries[username]['abnormal_count'] = username_label_counts.get(username, 0)

        # Extract the filtered entries' values to a list
        filtered_data_list = list(latest_entries.values())

        return JsonResponse({'data': filtered_data_list})
    return render(request, "Error/404.html")

def room_management_data_all_history(request, examID):
    exam_id = request.GET.get('exam_id', None)
    supervisor_username = request.session.get('user_name')
    if Exam_Management.objects.filter(supervisor=supervisor_username).exists():
        # Get the list of unique usernames
        unique_usernames = History_Management.objects.filter(
            erd_id__exam_id__supervisor__username=supervisor_username,
            erd_id__exam_id__exam_id=exam_id
        ).values_list('erd_id__username__username', flat=True).distinct()

        # Calculate the count of 'abnormal' label for each unique username
        username_label_counts = Counter(
            History_Management.objects.filter(
                erd_id__exam_id__supervisor__username=supervisor_username,
                erd_id__exam_id__exam_id=exam_id,
                labels='abnormal',
                erd_id__username__username__in=unique_usernames
            ).values_list('erd_id__username__username', flat=True)
        )

        query = History_Management.objects.filter(
            erd_id__exam_id__supervisor__username=supervisor_username,
            erd_id__exam_id__exam_id=exam_id
        ).order_by('-htime').values(
            'his_id',
            'htime',
            'labels',
            'erd_id',
            'erd_id__username__username',
            'erd_id__state',
            'erd_id__exam_id__exam_id',
            'erd_id__exam_id__course_id',
            'erd_id__exam_id__exam_date',
            'erd_id__exam_id__duration',
            'erd_id__exam_id__room_id',
            'erd_id__exam_id__supervisor__username',
        )

        # Add the 'abnormal_count' to each record in the queryset based on the counts
        for record in query:
            username = record['erd_id__username__username']
            record['abnormal_count'] = username_label_counts.get(username, 0)

        # Convert QuerySet to list for manipulation
        query_list = list(query)
        print(query_list)
        return JsonResponse({'data': query_list})
    return render(request, "Error/404.html")

def unlock_exam(request):
    if request.method == 'POST':
        history_id = request.POST.get('history_id')
        try:
            # Perform the logic to update label.txt here
            with open('token.txt', 'w') as label_file:
                label_file.write('0')

            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

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

def check_erd_id(request):
    if request.method == 'GET':
        try:
            erd_id = request.GET.get('erd_id', None)

            if erd_id is not None:
                # Check if the erd_id exists in the file
                with open('token.txt', 'r') as file:
                    erd_ids = [line.strip() for line in file]
                    exists = erd_id in erd_ids

                return JsonResponse({'exists': exists})
            else:
                return JsonResponse({'error': 'erd_id not provided in the query parameters.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': f'Error checking erd_id: {e}'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method. Only GET is allowed.'}, status=405)

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

def joined_backup(request):
    exam_id = request.GET.get('exam_id', '')
    context = {'exam_id': exam_id}
    return render(request, 'Dashboard_exam_room/joined.html',context)

def joined(request):
    exam_id = request.GET.get('exam_id', '')
    context = {'exam_id': exam_id}
    return render(request, 'Dashboard_exam_room/room_management_data.html',context)

def exam_room_1(request):
    # Check if the user is allowed to access the exam
    if not request.session.get('in_exam', False):
        # Redirect to a different page if the user is not in an exam
        return redirect('home')  # Replace 'home' with the name of your home page's URL pattern

    # Render the exam page
    return render(request, 'Exam_room/exam_room1.html')

def finish_exam(request):
    request.session['in_exam'] = False
    # Redirect to a different page after finishing the exam
    return redirect('home')  # Replace 'home' with your home page's URL pattern

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

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        phone = request.POST.get('phone') 
        random_string_length = 8

        if password == password2:
            if User_Management.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return redirect('register')
            else:
                # Create new user
                new_user = User_Management(
                    username=username,
                    upassword=password,
                    mail=email,
                    phone=phone,
                    remainday=0,  # Example default value
                    ucode=''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(random_string_length))  # Example default value
                    # utype is not specified here, so it will take the default value 'normal'
                )
                new_user.save()
                messages.success(request, "Your account has been created successfully")
                return redirect('login')  # Redirect to login page after registration
        else:
            messages.error(request, "Passwords do not match")
            return redirect('register')

    return render(request, 'Account/register.html')  # Render the registration page if not a POST request

def login(request):
    if 'user_name' in request.session:
        # User is logged in, render the course page
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        try:
            user = User_Management.objects.get(username=username, upassword=password)
            request.session['user_name'] = user.username  # Set a session variable
            request.session['utype'] = user.utype
            request.session['remainday'] = user.remainday
            # print("User Type:", request.session.get('utype'))
            # print("Remain Days:", request.session.get('remainday'))
            return redirect('home')
        except User_Management.DoesNotExist:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, "Account/login.html")

def changepassword(request):
    if 'user_name' not in request.session:
        # Redirect to login if the user is not logged in
        return redirect('login')

    if request.method == "POST":
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        try:
            user = User_Management.objects.get(username=request.session['user_name'])

            if user.upassword == current_password:
                if new_password == confirm_password:
                    # Update the password
                    user.upassword = new_password
                    user.save()
                    messages.success(request, "Password changed successfully.")
                    return redirect('changepassword')
                else:
                    messages.error(request, "New passwords do not match.")
            else:
                messages.error(request, "Current password is incorrect.")
        except User_Management.DoesNotExist:
            messages.error(request, "User not found.")

    return render(request, "Account/changepassword.html")

def logout(request):
    try:
        # Clear the session
        request.session.clear()
        messages.info(request, "You have been logged out successfully.")
    except KeyError:
        pass  # No session was found, which means user was not logged in
    # Redirect to the homepage or login page after logout
    return redirect('login')

@csrf_exempt
def tool_login_sdkjbaiuwq983y912u32186hsjzbguhcvwehui873y89n8y7s(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        text = username + '%' + password
        print(text)
        try:
            user = User_Management.objects.get(username = username)
            if user.upassword == password:
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
        text = username + '%' + password + '%' + exam_id + '%' + exam_code
        print(text)
        try:
            user = User_Management.objects.get(username = username)
            if user.upassword == password:
                try:
                    exam = Exam_Management.objects.get(exam_id = exam_id)
                    if exam.supervisor.ucode == exam_code:
                        erd_id = Exam_Room_Doing.objects.get(exam_id = exam_id, username = username)
                        erd_id = erd_id.erd_id
                        return HttpResponse(f'{erd_id}')
                    else:
                        return HttpResponse('False')
                except:
                    return HttpResponse('False')
        except:
            return HttpResponse('False')
    return render(request, "Error/404.html")

def history(request):
    histories = History_Management.objects.all()
    return render(request, 'Dashboard_exam_room/history.html', {'histories': histories})

def history_management(request):
    data = list(History_Management.objects.values('his_id', 'erd_id', 'htime', 'labels'))  # adjust fields as necessary
    
    return JsonResponse({'data': data})

def history_exam_join_view(request):
    supervisor_username = request.session.get('user_name') 
    # Query to join History_Management -> Exam_Room_Doing -> Exam_Management
    query = History_Management.objects.select_related('erd_id__exam_id').filter(erd_id__exam_id__supervisor__username=supervisor_username, labels='abnormal').values(
        'his_id',
        'htime',
        'labels',
        'erd_id',  # Access erd_id from Exam_Room_Doing
        'erd_id__username__username',  # Access username from User_Management via Exam_Room_Doing
        'erd_id__state',  # Access state from Exam_Room_Doing
        'erd_id__exam_id__exam_id',  # Access exam_id from Exam_Management
        'erd_id__exam_id__course_id',  # Access course_id from Exam_Management
        'erd_id__exam_id__exam_date',  # Access exam_date from Exam_Management
        'erd_id__exam_id__duration',  # Access duration from Exam_Management
        'erd_id__exam_id__room_id',  # Access room_id from Exam_Management
        'erd_id__exam_id__supervisor__username',  # Access supervisor username from User_Management via Exam_Management
    )

    data_list = list(query)
    return JsonResponse({'data': data_list})

def test(request):
    users = User_Management.objects.all()  # Retrieves all User_Management objects
    return render(request, 'Dashboard_exam_room/test.html', {'users': users})

def check_state(request):
    if request.method == 'GET':
        input_string = request.GET.get('inf', f'a%a')  # Default to 'a' if 'inf' is not provided
        check_status = input_string.split('%')
        print(check_status)
        current_time = datetime.now()
        current_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
        his_count = History_Management.objects.count()
        print(current_time)
        
        if check_status[1] == 'False':
            History_Management.objects.create(his_id=f'h{his_count+1}', erd_id=Exam_Room_Doing.objects.get(erd_id=f'{check_status[0]}'), htime=parse_datetime(f'{current_time}'), labels='normal')
        elif check_status[1] == 'True':
            History_Management.objects.create(his_id=f'h{his_count+1}', erd_id=Exam_Room_Doing.objects.get(erd_id=f'{check_status[0]}'), htime=parse_datetime(f'{current_time}'), labels='abnormal')
        
        # Get the directory of the current module
        current_directory = os.path.dirname(os.path.realpath(__file__))

        # Construct the path to the "token.txt" file in the parent directory
        token_file_path = os.path.join(current_directory, '..', 'token.txt')

        # Read the content of the file
        with open(token_file_path, "r") as file:
            text = file.read()
        return HttpResponse(text)
    return HttpResponse("b")


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

def chart(request): # Get all records from the database
    return render(request, 'Interface/chart.html')

def get_user_data(request):
    data = list(User_Management.objects.values('username', 'upassword', 'utype'))  # adjust fields as necessary
    return JsonResponse({'data': data})

def test_request(request):
    if request.method == "GET":
        # Extract client information
        client_ip = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT')
        referrer = request.META.get('HTTP_REFERER')

        # Log the information (you can replace this with your desired logging mechanism)
        print("Client IP:", client_ip)
        print("User agent:", user_agent)
        print("Referrer:", referrer)

    return HttpResponse('b')