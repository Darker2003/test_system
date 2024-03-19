import csv
import os
from django.core.management.base import BaseCommand
from Abnormal_behavior.models import User_Management, Bill, Exam_Management, Exam_Room_Doing, History_Management, Quotes

class Command(BaseCommand):
    help = 'Export data from Django models to CSV'

    def handle(self, *args, **kwargs):
        base_path = os.getcwd()  # Get the current working directory

        # Export User_Management data to CSV
        user_filename = os.path.join(base_path, 'User_Management.csv')
        self.export_to_csv(User_Management.objects.all(), user_filename, ['username', 'upassword', 'utype', 'remainday', 'ucode', 'mail', 'phone'])

        # Export Bill data to CSV
        bill_filename = os.path.join(base_path, 'Bill.csv')
        self.export_to_csv(Bill.objects.all(), bill_filename, ['bill_id', 'username_id', 'bill_date'])

        # Export Exam_Management data to CSV
        exam_filename = os.path.join(base_path, 'Exam_Management.csv')
        self.export_to_csv(Exam_Management.objects.all(), exam_filename, ['exam_id', 'course_id', 'exam_date', 'duration', 'room_id', 'supervisor_id'])

        # Export Exam_Room_Doing data to CSV
        exam_room_filename = os.path.join(base_path, 'Exam_Room_Doing.csv')
        self.export_to_csv(Exam_Room_Doing.objects.all(), exam_room_filename, ['erd_id', 'username_id', 'exam_id_id', 'state'])

        # Export History_Management data to CSV
        history_filename = os.path.join(base_path, 'History_Management.csv')
        self.export_to_csv(History_Management.objects.all(), history_filename, ['his_id', 'erd_id_id', 'htime', 'labels', 'state'])

        # Export Quotes data to CSV
        quotes_filename = os.path.join(base_path, 'Quotes.csv')
        self.export_to_csv(Quotes.objects.all(), quotes_filename, ['qid', 'qmail', 'qname', 'qphone', 'qadvise', 'qmessage'])

    def export_to_csv(self, queryset, filename, headers):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
            for item in queryset:
                writer.writerow([getattr(item, field) for field in headers])
        self.stdout.write(self.style.SUCCESS(f'Data exported to {filename} successfully!'))
