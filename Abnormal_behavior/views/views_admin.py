from django.shortcuts import render
from ..models import User_Management, History_Management, Exam_Management, Bill
from django.contrib.auth.decorators import user_passes_test

from django.http import JsonResponse
from django.db.models import Count, Case, When, IntegerField, Subquery, Value
from django.db.models.functions import  ExtractYear, ExtractMonth
from Abnormal_behavior.models import Exam_Management, Exam_Room_Doing, History_Management, User_Management, Bill
from datetime import timedelta

def chart(request): # Get all records from the database
    return render(request, 'Interface/chart.html')

def is_superuser(user):
    return user.is_authenticated and user.is_superuser

# Apply the user_passes_test decorator to the view
@user_passes_test(is_superuser, login_url='/admin/login/')
def dash_index(request):
    exam_ids = Exam_Management.objects.values_list('exam_id', flat=True).distinct()
    exam_name = []
    duration = []
    # Loop through each exam ID
    for exam_id in exam_ids:
        exam = Exam_Management.objects.get(exam_id=exam_id)
        exam_name.append(exam_id)
        duration.append(exam.duration)
    response_data = {
        'exam_name': sorted(exam_name),
        'duration': duration, 
    }
    return render(request, 'Dashboard_admin/index.html', {'dropdown_data': response_data['exam_name']})

def per_course(request): #pie chart 1
    # Subquery to filter exam room doings with abnormal history
    subquery = History_Management.objects.filter(
        labels='abnormal'
    ).values('erd_id')

    # Use Subquery to filter Exam_Room_Doing
    subquery = Subquery(subquery)
    violations_per_course = Exam_Room_Doing.objects.filter(
        erd_id__in=subquery
    ).values('exam_id__course_id').annotate(
        num_student=Count('username_id', distinct=True)
    )

    # Create lists to store course names and number of students
    course_names = []
    num_students = []

    # Extract course names and number of students per course
    for course in violations_per_course:
        course_names.append(course['exam_id__course_id'])
        num_students.append(course['num_student'])
    
    # Construct response data
    response_data = {
        'course_names': course_names,
        'num_students': num_students
    }

    # Return response as JSON
    return JsonResponse(response_data)

def per_proctor(request): #pie chart 2
    # Query to get the count of violations per supervisor
    violations_per_supervisor = Exam_Management.objects.filter(
        exam_room_doing__history_management__labels='abnormal'
    ).values('supervisor__username').annotate(
        num_students_abnormal=Count('exam_room_doing__username', distinct=True)
    )
    supervisor_name = []
    num_student_per_supervisor= []
        # Display the results
    for supervisor in violations_per_supervisor:
        supervisor_name.append(supervisor['supervisor__username'])
        num_student_per_supervisor.append(supervisor['num_students_abnormal'])
    # Construct response data
    response_data = {
        'supervisor_name': supervisor_name,
        'num_student_per_supervisor': num_student_per_supervisor
    }

    # Return response as JSON
    return JsonResponse(response_data)

def violation_report(request): #Multiple bar chart
    # Subquery to filter exam room doings with abnormal history
    subquery_abnormal = Exam_Room_Doing.objects.filter(
            history_management__labels='abnormal').values('exam_id')

        # Query to get the count of violations per course
    violations_per_course = Exam_Management.objects.filter(
    exam_id__in=subquery_abnormal
    ).values('course_id').annotate(
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
    course_name = []
    number_of_abnormal = []
    number_of_normal = []
    # Display the results
    for course in violations_per_course:
        course_name.append(course['course_id'])
        number_of_abnormal.append(course['num_abnormal_violations'])
        number_of_normal.append(course['num_normal_violations'])
     # Construct response data
    response_data = {
        'course_name': course_name,
        'number_of_abnormal': number_of_abnormal, 
        'number_of_normal': number_of_normal,
    }
    # Return response as JSON
    return JsonResponse(response_data)

def time_series_on_exam_id(self):
    # Query to count abnormal and normal behaviors for each exam at each timestamp
    exam_ids = Exam_Management.objects.values_list('exam_id', flat=True).distinct()
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
         # Construct response data
    response_data = {
        'exam_name': exam_name,
        'duration': duration,
        'number_of_abnormal': abnormal_count_on_exam_ids, 
        'number_of_normal': normal_count_on_exam_ids,
    }
    # Return response as JSON
    return JsonResponse(response_data)
    
def business_index(request):
    user_counts = User_Management.objects.aggregate(
            total_users=Count('username', distinct=True),
            normal_users=Count(Case(When(utype='normal', then=Value(1)), output_field=IntegerField())),
            vip_users=Count(Case(When(utype='vip', then=Value(1)), output_field=IntegerField()))
        )
    total_users = user_counts['total_users']
    vip_user = user_counts['vip_users']
    non_vip_user = user_counts['normal_users']

    bill_count = Bill.objects.count()
    total_room = Exam_Management.objects.count()
    total_abnormal = History_Management.objects.filter(labels = 'abnormal').count()

    context = {
        'first_name': request.user.first_name,
        'total_users': total_users,
        'vip_user': vip_user,
        'non_vip_user': non_vip_user,
        'bill_count': bill_count,
        'total_room': total_room,
        'total_abnormal':  total_abnormal,
    }
    return render(request, 'Dashboard_admin/index_business.html', context)

def vip_timeseries(self): #display number of vip user by year and month 
    # Query to count the number of VIP users by purchase year
    vip_users_by_year = Bill.objects.filter(
        username__utype='vip'
    ).annotate(
        purchase_year=ExtractYear('bill_date')
    ).values(
        'purchase_year'
    ).annotate(
        num_vip_users=Count('username', distinct=True)
    )
    purchased_year = []
    num_vip_users_year = []
    # Display the results
    for data in vip_users_by_year:
        purchased_year.append(data['purchase_year'])
        num_vip_users_year.append(data['num_vip_users'])

    # Query to count the number of VIP users by purchase month
    vip_users_by_month = Bill.objects.filter(
        username__utype='vip'
    ).annotate(
        purchase_month=ExtractMonth('bill_date')
    ).values(
        'purchase_month'
    ).annotate(
        num_vip_users=Count('username', distinct=True)
    )

    purchased_month = []
    num_vip_users_month = []
    # Display the results
    for data in vip_users_by_month:
        purchased_month.append(data['purchase_month'])
        num_vip_users_month.append(data['num_vip_users'])

    response_data = {
    'purchased_year': purchased_year,
    'num_vip_users_year': num_vip_users_year,
    'purchased_month': purchased_month,
    'num_vip_users_month': num_vip_users_month,
}
    # Return response as JSON
    return JsonResponse(response_data)
    