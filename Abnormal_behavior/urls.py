from django.urls import path
from django.contrib.auth import views as auth_views 
from .views import *
# from .views import views_create_examroom

urlpatterns = [
    #General interface
    path('', views_interfaces.home, name='home'),
    path('about',views_interfaces.about, name='about'),
    path('course',views_interfaces.course, name='course'),
    path('price',views_interfaces.price, name='price'),
    path('feature',views_interfaces.feature, name='feature'),
    path('team',views_interfaces.team, name='team'),
    path('testimonial',views_interfaces.testimonial, name='testimonial'),
    path('quote',views_interfaces.quote, name='quote'),
    path('contact',views_interfaces.contact, name='contact'),
    
    #Account
    path('login',views_account.login, name='login'),
    path('register',views_account.register, name='register'),
    path('changepassword',views_account.changepassword, name='changepassword'),
    path('logout/', views_account.logout, name='logout'),
    path('forgot_password',views_account.forgot_password, name='forgot_password'),
    path('reset-password/<str:username>/<str:token>/', views_account.reset_password, name='reset_password'),

    
    #Exam room interface
    path('finish_exam', views_exam.finish_exam, name='finish_exam'),
    path('exam_menu',views_exam.exam_menu, name='exam_menu'),
    path('save_quiz',views_exam.save_quiz, name='save_quiz'),
    
    #Exam room function
    path('create_new_room',views_exam_function.create_new_room, name='create_new_room'),
    path('quiz',views_exam_function.quiz, name='quiz'),
    path('access_room',views_exam_function.access_room, name='access_room'),
    path('exam_room/<str:exam_id>/', views_exam_function.exam_room, name='exam_room'),
   

    #Exam dashboard
    path('list_exam_room_available', views_exam_dashboard.list_exam_room_available, name='list_exam_room_available'),
    path('doing_exam_room',views_exam_dashboard.doing_exam_room, name='doing_exam_room'),
    path('get_exam_room_doing_list', views_exam_dashboard.exam_room_doing_list, name='get_exam_room_doing_list'),
    path('showall/<str:examID>/', views_exam_dashboard.room_management_data_all_history, name='room_management_data_all_history'),
    path('<str:examID>/', views_exam_dashboard.room_management_data, name='room_management_data'),
    path('joined', views_exam_dashboard.joined, name='joined'),
    path('check_erd_id', views_exam_dashboard.check_erd_id, name='check_erd_id'),
    path('unlock_exam', views_exam_dashboard.unlock_exam, name='unlock_exam'),
    path('report_on_exam', views_exam_dashboard.report_on_exam, name='report_on_exam'),
    
    #Tool
    path('write_token', views_tool.write_token, name='write_token'),
    path('tool_login_sdkjbaiuwq983y912u32186hsjzbguhcvwehui873y89n8y7s',views_tool.tool_login_sdkjbaiuwq983y912u32186hsjzbguhcvwehui873y89n8y7s, name='tool_login_sdkjbaiuwq983y912u32186hsjzbguhcvwehui873y89n8y7s'),
    path('exam_login_sjdby18h27ndwn7y127t3672wcdawd1jdfkk009saidjw8890jwhau',views_tool.exam_login_sjdby18h27ndwn7y127t3672wcdawd1jdfkk009saidjw8890jwhau, name='exam_login_sjdby18h27ndwn7y127t3672wcdawd1jdfkk009saidjw8890jwhau'),
    path("check_status_jaghfuie19sba872t1dnx1y278yn7tx176bn27txb67n1xg7rfxbd5", views_tool.check_state_jaghfuie19sba872t1dnx1y278yn7tx176bn27txb67n1xg7rfxbd5, name='check_status_jaghfuie19sba872t1dnx1y278yn7tx176bn27txb67n1xg7rfxbd5'),
    path('upload', views_tool.upload_img, name='upload'),
    path('unlock_jiuhduigaiugyueihdg19y7e61hdtg76badr56n816nb2t5c7ecne8t72nd', views_tool.unlock_jiuhduigaiugyueihdg19y7e61hdtg76badr56n816nb2t5c7ecne8t72nd, name='unlock_jiuhduigaiugyueihdg19y7e61hdtg76badr56n816nb2t5c7ecne8t72nd'),
    
    #Admin dash
    path('chart', views_admin.chart, name='chart'),
    path('quotes',  views_service.quotes, name='quotes'),

    path('dash_index', views_admin.dash_index, name='dash_index'),
    path('per_course', views_admin.per_course, name='per_course'), #pie chart 
    path('per_proctor', views_admin.per_proctor, name='per_proctor'), #pie chart 2
    path('violation_report', views_admin.violation_report, name='violation_report'), #multiple bar chart time_series_on_exam_id
    path('time_series_on_exam_id', views_admin.time_series_on_exam_id, name='time_series_on_exam_id'), #time_series_on_exam_id

    path('business_index', views_admin.business_index, name='business_index'),
    path('vip_timeseries', views_admin.vip_timeseries, name='vip_timeseries'),
    path('vip_timeseries', views_admin.vip_timeseries, name='vip_timeseries'),
    # path('upload', views_create_examroom.upload, name='upload'),
    
]
