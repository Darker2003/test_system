from django.contrib import admin
from .models import User_Management, Bill, Exam_Management, Exam_Room_Doing, History_Management, Quotes, Quiz

admin.site.register(User_Management)
admin.site.register(Bill)
admin.site.register(Exam_Management)
admin.site.register(Exam_Room_Doing)
admin.site.register(History_Management)
admin.site.register(Quotes)
admin.site.register(Quiz)
