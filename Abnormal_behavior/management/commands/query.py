from django.core.management.base import BaseCommand
from django.db.models import Count, Case, When, IntegerField, Subquery, Value
from django.db.models.functions import  ExtractYear, ExtractMonth
from Abnormal_behavior.models import Exam_Management, Exam_Room_Doing, History_Management, User_Management, Bill, Quiz
from datetime import timedelta
 
class Command(BaseCommand):
    help = 'Displays the number of violations per exam'
 
    def handle(self, *args, **kwargs):
        # self.abnormal_flcourse()
        # self.protors()
        # self.state_of_student_flcourse()
        # self.display_behavior_counts()
        # self.display_user_service_counts()
        # self.display_vip_users_by_year()
        # self.display_vip_users_by_month()
        # self.display_vip_purchases_by_user_and_year()
        # self.display_remaining_days_for_vip_users()
        # self.display_vip_users_info()
        # self.display_instructors_with_vip_accounts()
        self.submit_quiz()
 
    def abnormal_flcourse(self): # số lượng sinh viên abnoraml/course
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
 
        # Display the results
        course_name = []
        num_student_per_course = []
        for course in violations_per_course:
            course_name.append(course['exam_id__course_id'])
            num_student_per_course.append(course['num_student'])
        print(course_name)
        print(num_student_per_course)
    
    def protors(self): # số lượng sinh viên abnoraml/proctors
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
        print(supervisor_name)
        print(num_student_per_supervisor)
        
 
    def state_of_student_flcourse(self): # số lượng sinh viên abnoraml/normal cua course
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
        print(course_name)
        print(number_of_abnormal)
        print(number_of_normal)


    def display_behavior_counts(self): 
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
                
                #exam_name.append(exam_id)
                abnormal_count_on_exam.append(abnormal_count)
                normal_count_on_exam.append(normal_count)
                #Print the result
                # self.stdout.write(self.style.SUCCESS(
                #     f"Exam ID: {exam_id}, Timestamp: {current_time}, "
                #     f"Abnormal Count: {abnormal_count}, Normal Count: {normal_count}"
                # ))
 
                # Move to the next minute
                current_time += timedelta(minutes=1)
            abnormal_count_on_exam_ids.append(abnormal_count_on_exam)
            normal_count_on_exam_ids.append(normal_count_on_exam)
        print(exam_name)
        print(duration)
        print(abnormal_count_on_exam_ids)
        print(normal_count_on_exam_ids)
        
    def display_user_service_counts(self):
        total_users = []
        vip_users = []
        normal_users = []
        # Query to count total users and users based on their service types
        user_counts = User_Management.objects.aggregate(
            total_users=Count('username', distinct=True),
            normal_users=Count(Case(When(utype='normal', then=Value(1)), output_field=IntegerField())),
            vip_users=Count(Case(When(utype='vip', then=Value(1)), output_field=IntegerField()))
        )
        total_users = user_counts['total_users']
        vip_users = user_counts['vip_users']
        normal_users = user_counts['normal_users']

        print(total_users)
        print(vip_users)
        print(normal_users)

    def display_vip_users_by_year(self):
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
        num_vip_users = []
        # Display the results
        for data in vip_users_by_year:
            purchased_year.append(data['purchase_year'])
            num_vip_users.append(data['num_vip_users'])
        print(purchased_year)
        print(num_vip_users)
            
    def display_vip_users_by_month(self):
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
        num_vip_users = []
        # Display the results
        for data in vip_users_by_month:
            purchased_month.append(data['purchase_month'])
            num_vip_users.append(data['num_vip_users'])
        print(purchased_month)
        print(num_vip_users)
            
    def display_vip_purchases_by_user_and_year(self):
        # Query to count the number of VIP purchases for each user in a year
        vip_purchases_by_user_and_year = Bill.objects.filter(
            username__utype='vip'
        ).annotate(
            purchase_year=ExtractYear('bill_date')
        ).values(
            'username', 'purchase_year'
        ).annotate(
            num_purchases=Count('bill_id')
        ).order_by(
            'username', 'purchase_year'
        )

        # Display the results
        for data in vip_purchases_by_user_and_year:
            self.stdout.write(self.style.SUCCESS(
                f"Username: {data['username']}, Purchase Year: {data['purchase_year']}, Number of Purchases: {data['num_purchases']}"
            ))
            
    def display_remaining_days_for_vip_users(self):
        # Query to get the remaining days for each user with a VIP account
        vip_users_with_remaining_days = User_Management.objects.filter(
            utype='vip',
            remainday__gt=0
        ).values(
            'username', 'remainday'
        )

        # Display the results
        for data in vip_users_with_remaining_days:
            self.stdout.write(self.style.SUCCESS(
                f"Username: {data['username']}, Remaining Days: {data['remainday']}"
            ))
            
    def display_vip_users_info(self):
        # Query to get information about users with VIP accounts
        vip_users_info = User_Management.objects.filter(
            utype='vip'
        ).values(
            'username', 'upassword', 'ucode', 'mail', 'phone'
        ).distinct()

        # Display the results
        for data in vip_users_info:
            self.stdout.write(self.style.SUCCESS(
                f"Username: {data['username']}, Password: {data['upassword']}, Code: {data['ucode']}, Email: {data['mail']}, Phone: {data['phone']}"
            ))
            
    def display_instructors_with_vip_accounts(self):
        # Query to get information about instructors who have purchased VIP accounts
        instructors_with_vip_accounts = User_Management.objects.filter(
            exam_management__supervisor__utype='vip'
        ).values(
            'username', 'upassword', 'ucode', 'mail', 'phone'
        ).distinct()

        # Display the results
        for data in instructors_with_vip_accounts:
            self.stdout.write(self.style.SUCCESS(
                f"Username: {data['username']}, Password: {data['upassword']}, Code: {data['ucode']}, Email: {data['mail']}, Phone: {data['phone']}"
            ))
                




