from django.shortcuts import render
from django.http import JsonResponse
from ..models import History_Management, Exam_Management, Exam_Room_Doing
from collections import Counter
from django.db.models import Count, Case, When, IntegerField, Subquery, Value
from datetime import datetime, timedelta
# Create your views here.
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
        # print(query_list)
        return JsonResponse({'data': query_list})
    return render(request, "Error/404.html")

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

def joined(request):
    exam_id = request.GET.get('exam_id', '')
    context = {'exam_id': exam_id}
    return render(request, 'Dashboard_exam_room/room_management_data.html',context)

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

def report_on_exam(request): # số lượng sinh viên abnoraml/normal cua course
    exam_id_from_user = request.GET.get('exam_id', '')
    # Subquery to filter exam room doings with abnormal history
    subquery_abnormal = Exam_Room_Doing.objects.values_list('exam_id', flat=True).distinct()
    subquery_abnormal = sorted(subquery_abnormal)
    # Query to get the count of violations per course
    violations_per_course = Exam_Management.objects.filter(
    exam_id__in=subquery_abnormal
    ).values('exam_id').annotate(
            num_abnormal_violations=Count(
                Case(
                    When(
                        exam_room_doing__history_management__labels='abnormal',
                        then=1
                    ),
                    output_field=IntegerField()
                )
            ),
            num_normal_violations=Count(
                Case(
                    When(
                        exam_room_doing__history_management__labels='normal',
                        then=1
                    ),
                    output_field=IntegerField()
                )
            )
        )
    exam_id = []
    number_of_abnormal = []
    number_of_normal = []
    # Display the results
    for course in violations_per_course:
        exam_id.append(course['exam_id'])
        number_of_abnormal.append(course['num_abnormal_violations'])
        number_of_normal.append(course['num_normal_violations'])
    response_data1 = {
    'exam_id_from_user': exam_id_from_user,
    'exam_id': exam_id,
    'number_of_abnormal': number_of_abnormal,
    'number_of_normal': number_of_normal,
    }

    # Query to count abnormal and normal behaviors for each exam at each timestamp
    exam_ids = Exam_Room_Doing.objects.values_list('exam_id', flat=True).distinct()
    exam_ids = sorted(exam_ids)
    exam_name = []
    duration = []
    abnormal_count_on_exam_ids = []
    normal_count_on_exam_ids = []
    # Loop through each exam ID
    for exam_id in exam_ids:
        exam = Exam_Management.objects.get(exam_id=exam_id)
        exam_start = exam.exam_date
        exam_end = exam_start + timedelta(minutes=exam.duration)
        exam_name.append(exam_id)
        duration.append(exam.duration)
        abnormal_count_on_exam = []
        normal_count_on_exam = []
        # Loop through each minute within the exam duration
        current_time = exam_start
        while current_time <= exam_end:
            # Define the start and end of the minute interval
            interval_start = current_time
            interval_end = current_time + timedelta(minutes=1)

            # Count abnormal and normal states for each minute
            abnormal_count = History_Management.objects.filter(
                erd_id__exam_id=exam_id,
                htime__gte=interval_start,
                htime__lt=interval_end,
                labels='abnormal'
            ).count()
            normal_count = History_Management.objects.filter(
                erd_id__exam_id=exam_id,
                htime__gte=interval_start,
                htime__lt=interval_end,
                labels='normal'
            ).count()
            
            abnormal_count_on_exam.append(abnormal_count)
            normal_count_on_exam.append(normal_count)
            # Move to the next minute
            current_time += timedelta(minutes=1)
    
        abnormal_count_on_exam_ids.append(abnormal_count_on_exam)
        normal_count_on_exam_ids.append(normal_count_on_exam)
    response_data2 = {
        'exam_name': exam_name,
        'duration': duration,
        'number_of_abnormal_time_series': abnormal_count_on_exam_ids, 
        'number_of_normal_time_series': normal_count_on_exam_ids,
    }
    response_data = {**response_data1, **response_data2}
    # Return response as JSON
    return JsonResponse(response_data)

    
