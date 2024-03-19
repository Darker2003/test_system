
import csv
import os
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime
from Abnormal_behavior.models import User_Management, Bill, Exam_Management, Exam_Room_Doing, History_Management, Quotes

class Command(BaseCommand):
    help = 'Inserts data from CSV files into the database'

    def handle(self, *args, **options):
        base_path = os.getcwd()  # Get the current working directory

        # CSV filenames
        csv_files = [
            ('Data/User_Management.csv', User_Management),
            ('Data/Bill.csv', Bill),
            ('Data/Exam_Management.csv', Exam_Management),
            ('Data/Exam_Room_Doing.csv', Exam_Room_Doing),
            ('Data/History_Management.csv', History_Management),
            ('Data/Quotes.csv', Quotes)
        ]

        for filename, model in csv_files:
            csv_filepath = os.path.join(base_path, filename)
            with open(csv_filepath, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    model.objects.create(**row)

        self.stdout.write(self.style.SUCCESS('Data inserted from CSV files successfully!'))
        
        
# from django.core.management.base import BaseCommand
# from django.utils.dateparse import parse_datetime
# from Abnormal_behavior.models import User_Management, Bill, Exam_Management, Exam_Room_Doing, History_Management
# from django.utils.dateparse import parse_datetime
# class Command(BaseCommand):
#     help = 'Inserts data into the database'

#     def handle(self, *args, **options):
#         # Insert data into User_Management model
#         User_Management.objects.create(username='dat', upassword='123', utype='Vip', remainday=18, ucode='18xma9', mail='dat@gmail.com', phone='0123456789')
#         User_Management.objects.create(username='an', upassword='123', utype='Normal', remainday=0, ucode='33xma9', mail='an@gmail.com', phone='0123456789')
#         User_Management.objects.create(username='hoan', upassword='456', utype='Vip', remainday=19, ucode='45daa9', mail='hoan@gmail.com', phone='0123456790')
#         User_Management.objects.create(username='bao', upassword='456', utype='Normal', remainday=0, ucode='98mla3', mail='bao@gmail.com', phone='0123456791')
#         User_Management.objects.create(username='chi', upassword='789', utype='Vip', remainday=30, ucode='67ads1', mail='chi@gmail.com', phone='0123456792')
#         User_Management.objects.create(username='khang', upassword='789', utype='Vip', remainday=30, ucode='89jdk1', mail='khang@gmail.com', phone='0123456793')
#         User_Management.objects.create(username='hung', upassword='2345', utype='Vip', remainday=30, ucode='90fso0', mail='hung@gmail.com', phone='0123456794')
#         User_Management.objects.create(username='chien', upassword='13441', utype='vip', remainday=30, ucode='11dgs6', mail='chien@gmail.com0', phone='0234569157')
        
#         User_Management.objects.create(username='thanh', upassword='345', utype='Normal', remainday=0, ucode='78lma2', mail='thanh@gmail.com', phone='0123456795')
#         # User_Management.objects.create(username='linh', upassword='3456', utype='Vip', remainday=25, ucode='23nma5', mail='linh@gmail.com', phone='0123456796')
#         User_Management.objects.create(username='huyen', upassword='34567', utype='Normal', remainday=0, ucode='12qma8', mail='huyen@gmail.com', phone='0123456797')
#         User_Management.objects.create(username='minh', upassword='23456', utype='Vip', remainday=28, ucode='09dma3', mail='minh@gmail.com', phone='0123456798')
#         User_Management.objects.create(username='trung', upassword='987', utype='Vip', remainday=30, ucode='34sda6', mail='trung@gmail.com', phone='0123456799')
#         User_Management.objects.create(username='tuan', upassword='678', utype='Normal', remainday=0, ucode='45ama7', mail='tuan@gmail.com', phone='0123456800')
#         User_Management.objects.create(username='loan', upassword='12345', utype='Vip', remainday=30, ucode='89dca1', mail='loan@gmail.com', phone='0123456801')
#         User_Management.objects.create(username='phuong', upassword='123456', utype='Normal', remainday=0, ucode='23jka9', mail='phuong@gmail.com', phone='0123456802')
        
#         User_Management.objects.create(username='quang', upassword='234567', utype='Vip', remainday=29, ucode='56mla0', mail='quang@gmail.com', phone='0123456803')
#         User_Management.objects.create(username='mai', upassword='345678', utype='Normal', remainday=0, ucode='67ajs5', mail='mai@gmail.com', phone='0123456804')
#         User_Management.objects.create(username='linh', upassword='456789', utype='Vip', remainday=30, ucode='90lks1', mail='linh2@gmail.com', phone='0123456805')
#         User_Management.objects.create(username='hoa', upassword='567890', utype='Normal', remainday=0, ucode='89dmc3', mail='hoa@gmail.com', phone='0123456806')
#         User_Management.objects.create(username='thao', upassword='1234567', utype='Vip', remainday=30, ucode='23dmk7', mail='thao@gmail.com', phone='0123456807')
#         User_Management.objects.create(username='hieu', upassword='2345678', utype='Vip', remainday=30, ucode='67jka8', mail='hieu@gmail.com', phone='0123456808')
#         User_Management.objects.create(username='nhan', upassword='3456789', utype='Normal', remainday=0, ucode='34mka9', mail='nhan@gmail.com', phone='0123456809')
#         # User_Management.objects.create(username='thanh', upassword='4567890', utype='Vip', remainday=30, ucode='12ajd1', mail='thanh2@gmail.com', phone='0123456810')



#         # Insert data into Bill model
#         Bill.objects.create(bill_id='bdat1', username=User_Management.objects.get(username='dat'), bill_date=parse_datetime('2023-12-03 08:00:00'))
#         Bill.objects.create(bill_id='bhoan1', username=User_Management.objects.get(username='hoan'), bill_date=parse_datetime('2023-12-05 14:30:00'))
#         Bill.objects.create(bill_id='bdat2', username=User_Management.objects.get(username='dat'), bill_date=parse_datetime('2024-01-10 10:45:00'))
#         Bill.objects.create(bill_id='bhoan2', username=User_Management.objects.get(username='hoan'), bill_date=parse_datetime('2024-01-11 18:15:00'))
#         Bill.objects.create(bill_id='bchi1', username=User_Management.objects.get(username='chi'), bill_date=parse_datetime('2024-01-22 12:00:00'))
#         Bill.objects.create(bill_id='bchien1', username=User_Management.objects.get(username='chien'), bill_date=parse_datetime('2024-01-22 13:05:00'))
#         Bill.objects.create(bill_id='bkhang1', username=User_Management.objects.get(username='khang'), bill_date=parse_datetime('2024-01-23 12:00:00'))
#         Bill.objects.create(bill_id='bhung1', username=User_Management.objects.get(username='hung'), bill_date=parse_datetime('2024-01-23 12:00:00'))
#         Bill.objects.create(bill_id='bhoan3', username=User_Management.objects.get(username='hoan'), bill_date=parse_datetime('2024-02-15 18:15:00'))
#         Bill.objects.create(bill_id='bhoan4', username=User_Management.objects.get(username='hoan'), bill_date=parse_datetime('2024-03-18 15:15:00'))

#         # Bill.objects.create(bill_id='blinh1', username=User_Management.objects.get(username='linh'), bill_date=parse_datetime('2024-02-23 08:00:00'))
#         Bill.objects.create(bill_id='bminh1', username=User_Management.objects.get(username='minh'), bill_date=parse_datetime('2024-02-24 14:30:00'))
#         Bill.objects.create(bill_id='btrung1', username=User_Management.objects.get(username='trung'), bill_date=parse_datetime('2024-02-25 10:45:00'))
#         Bill.objects.create(bill_id='bloan1', username=User_Management.objects.get(username='loan'), bill_date=parse_datetime('2024-02-26 18:15:00'))
        
#         Bill.objects.create(bill_id='bquang1', username=User_Management.objects.get(username='quang'), bill_date=parse_datetime('2024-03-02 08:00:00'))
#         Bill.objects.create(bill_id='blinh1', username=User_Management.objects.get(username='linh'), bill_date=parse_datetime('2024-03-03 14:30:00'))
#         Bill.objects.create(bill_id='bthao1', username=User_Management.objects.get(username='thao'), bill_date=parse_datetime('2024-03-04 10:45:00'))
#         Bill.objects.create(bill_id='bhieu1', username=User_Management.objects.get(username='hieu'), bill_date=parse_datetime('2024-03-05 18:15:00'))
#         Bill.objects.create(bill_id='bthanh1', username=User_Management.objects.get(username='thanh'), bill_date=parse_datetime('2024-03-06 12:00:00'))
        
        
#         # Insert data into Exam_Management model
#         Exam_Management.objects.create(exam_id='emae1011', course_id='MAE101', exam_date=parse_datetime('2023-12-23 15:00:00'), duration=60, room_id='402', supervisor=User_Management.objects.get(username='khang'))
#         Exam_Management.objects.create(exam_id='emae1012', course_id='MAE101', exam_date=parse_datetime('2023-12-23 15:00:00'), duration=60, room_id='403', supervisor=User_Management.objects.get(username='chien'))
#         Exam_Management.objects.create(exam_id='emae1013', course_id='MAE101', exam_date=parse_datetime('2023-12-23 15:00:00'), duration=60, room_id='404', supervisor=User_Management.objects.get(username='hung'))
#         Exam_Management.objects.create(exam_id='emad1011', course_id='MAD101', exam_date=parse_datetime('2023-12-24 14:00:00'), duration=60, room_id='404', supervisor=User_Management.objects.get(username='khang'))
#         Exam_Management.objects.create(exam_id='eswe201c', course_id='SWE201c', exam_date=parse_datetime('2023-12-26 09:00:00'), duration=90, room_id='402', supervisor=User_Management.objects.get(username='hung'))
#         Exam_Management.objects.create(exam_id='emas1011', course_id='MAS101', exam_date=parse_datetime('2023-12-26 16:00:00'), duration=45, room_id='402', supervisor=User_Management.objects.get(username='hung'))
        
#         Exam_Management.objects.create(exam_id='emai3911', course_id='MAI391', exam_date=parse_datetime('2023-12-29 07:00:00'), duration=45, room_id='409', supervisor=User_Management.objects.get(username='khang'))
#         Exam_Management.objects.create(exam_id='emai3912', course_id='MAI391', exam_date=parse_datetime('2023-12-29 09:00:00'), duration=45, room_id='409', supervisor=User_Management.objects.get(username='chien'))
#         Exam_Management.objects.create(exam_id='emas1012', course_id='MAS101', exam_date=parse_datetime('2023-12-26 12:00:00'), duration=45, room_id='403', supervisor=User_Management.objects.get(username='chien'))
        
        
#         # Insert data into Exam_Room_Doing model
#         # Exam_Room_Doing.objects.create(erd_id='erd1', username=User_Management.objects.get(username='dat'), exam_id=Exam_Management.objects.get(exam_id='emae1011'), state='online')
#         # Exam_Room_Doing.objects.create(erd_id='erd2', username=User_Management.objects.get(username='an'), exam_id=Exam_Management.objects.get(exam_id='emae1011'), state='online')
#         # Exam_Room_Doing.objects.create(erd_id='erd3', username=User_Management.objects.get(username='hoan'), exam_id=Exam_Management.objects.get(exam_id='emae1012'), state='online')
#         # Exam_Room_Doing.objects.create(erd_id='erd4', username=User_Management.objects.get(username='bao'), exam_id=Exam_Management.objects.get(exam_id='emae1012'), state='online')
#         # Exam_Room_Doing.objects.create(erd_id='erd5', username=User_Management.objects.get(username='chi'), exam_id=Exam_Management.objects.get(exam_id='emad1011'), state='offline')
#         # Exam_Room_Doing.objects.create(erd_id='erd6', username=User_Management.objects.get(username='bao'), exam_id=Exam_Management.objects.get(exam_id='eswe201c'), state='online')
#         # Exam_Room_Doing.objects.create(erd_id='erd7', username=User_Management.objects.get(username='chi'), exam_id=Exam_Management.objects.get(exam_id='eswe201c'), state='online')
#         # Exam_Room_Doing.objects.create(erd_id='erd8', username=User_Management.objects.get(username='chi'), exam_id=Exam_Management.objects.get(exam_id='emas101'), state='offline')
#         # Exam_Room_Doing.objects.create(erd_id='erd9', username=User_Management.objects.get(username='hoan'), exam_id=Exam_Management.objects.get(exam_id='emas101'), state='online')
        
#         # Exam 1: emae1011
#         # Exam 1: emae1011
#         Exam_Room_Doing.objects.create(erd_id='erd1', username=User_Management.objects.get(username='dat'), exam_id=Exam_Management.objects.get(exam_id='emae1011'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd2', username=User_Management.objects.get(username='an'), exam_id=Exam_Management.objects.get(exam_id='emae1011'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd3', username=User_Management.objects.get(username='thanh'), exam_id=Exam_Management.objects.get(exam_id='emae1011'), state='offline')
#         Exam_Room_Doing.objects.create(erd_id='erd4', username=User_Management.objects.get(username='minh'), exam_id=Exam_Management.objects.get(exam_id='emae1011'), state='offline')
#         Exam_Room_Doing.objects.create(erd_id='erd5', username=User_Management.objects.get(username='hoa'), exam_id=Exam_Management.objects.get(exam_id='emae1011'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd6', username=User_Management.objects.get(username='nhan'), exam_id=Exam_Management.objects.get(exam_id='emae1011'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd7', username=User_Management.objects.get(username='hieu'), exam_id=Exam_Management.objects.get(exam_id='emae1011'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd8', username=User_Management.objects.get(username='thao'), exam_id=Exam_Management.objects.get(exam_id='emae1011'), state='offline')
#         Exam_Room_Doing.objects.create(erd_id='erd9', username=User_Management.objects.get(username='linh'), exam_id=Exam_Management.objects.get(exam_id='emae1011'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd10', username=User_Management.objects.get(username='quang'), exam_id=Exam_Management.objects.get(exam_id='emae1011'), state='online')

#         # Exam 2: emae1012
#         Exam_Room_Doing.objects.create(erd_id='erd11', username=User_Management.objects.get(username='hoan'), exam_id=Exam_Management.objects.get(exam_id='emae1012'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd12', username=User_Management.objects.get(username='bao'), exam_id=Exam_Management.objects.get(exam_id='emae1012'), state='offline')
#         Exam_Room_Doing.objects.create(erd_id='erd13', username=User_Management.objects.get(username='linh'), exam_id=Exam_Management.objects.get(exam_id='emae1012'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd14', username=User_Management.objects.get(username='mai'), exam_id=Exam_Management.objects.get(exam_id='emae1012'), state='offline')
#         Exam_Room_Doing.objects.create(erd_id='erd15', username=User_Management.objects.get(username='chi'), exam_id=Exam_Management.objects.get(exam_id='emae1012'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd16', username=User_Management.objects.get(username='linh'), exam_id=Exam_Management.objects.get(exam_id='emae1012'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd17', username=User_Management.objects.get(username='thanh'), exam_id=Exam_Management.objects.get(exam_id='emae1012'), state='offline')
#         Exam_Room_Doing.objects.create(erd_id='erd18', username=User_Management.objects.get(username='an'), exam_id=Exam_Management.objects.get(exam_id='emae1012'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd19', username=User_Management.objects.get(username='huyen'), exam_id=Exam_Management.objects.get(exam_id='emae1012'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd20', username=User_Management.objects.get(username='bao'), exam_id=Exam_Management.objects.get(exam_id='emae1012'), state='online')

#         # Exam 3: emae1013
#         Exam_Room_Doing.objects.create(erd_id='erd21', username=User_Management.objects.get(username='thanh'), exam_id=Exam_Management.objects.get(exam_id='emae1013'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd22', username=User_Management.objects.get(username='minh'), exam_id=Exam_Management.objects.get(exam_id='emae1013'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd23', username=User_Management.objects.get(username='huyen'), exam_id=Exam_Management.objects.get(exam_id='emae1013'), state='offline')
#         Exam_Room_Doing.objects.create(erd_id='erd24', username=User_Management.objects.get(username='hoa'), exam_id=Exam_Management.objects.get(exam_id='emae1013'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd25', username=User_Management.objects.get(username='nhan'), exam_id=Exam_Management.objects.get(exam_id='emae1013'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd26', username=User_Management.objects.get(username='hieu'), exam_id=Exam_Management.objects.get(exam_id='emae1013'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd27', username=User_Management.objects.get(username='thao'), exam_id=Exam_Management.objects.get(exam_id='emae1013'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd28', username=User_Management.objects.get(username='linh'), exam_id=Exam_Management.objects.get(exam_id='emae1013'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd29', username=User_Management.objects.get(username='quang'), exam_id=Exam_Management.objects.get(exam_id='emae1013'), state='offline')
#         Exam_Room_Doing.objects.create(erd_id='erd30', username=User_Management.objects.get(username='mai'), exam_id=Exam_Management.objects.get(exam_id='emae1013'), state='online')
        
#         # Exam 4: emad1011
#         Exam_Room_Doing.objects.create(erd_id='erd31', username=User_Management.objects.get(username='linh'), exam_id=Exam_Management.objects.get(exam_id='emad1011'), state='offline')
#         Exam_Room_Doing.objects.create(erd_id='erd32', username=User_Management.objects.get(username='minh'), exam_id=Exam_Management.objects.get(exam_id='emad1011'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd33', username=User_Management.objects.get(username='hoan'), exam_id=Exam_Management.objects.get(exam_id='emad1011'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd34', username=User_Management.objects.get(username='minh'), exam_id=Exam_Management.objects.get(exam_id='emad1011'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd35', username=User_Management.objects.get(username='quang'), exam_id=Exam_Management.objects.get(exam_id='emad1011'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd36', username=User_Management.objects.get(username='hieu'), exam_id=Exam_Management.objects.get(exam_id='emad1011'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd37', username=User_Management.objects.get(username='hoa'), exam_id=Exam_Management.objects.get(exam_id='emad1011'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd38', username=User_Management.objects.get(username='thanh'), exam_id=Exam_Management.objects.get(exam_id='emad1011'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd39', username=User_Management.objects.get(username='minh'), exam_id=Exam_Management.objects.get(exam_id='emad1011'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd40', username=User_Management.objects.get(username='hoa'), exam_id=Exam_Management.objects.get(exam_id='emad1011'), state='online')
        
#         # Exxam 5: eswe201c
#         Exam_Room_Doing.objects.create(erd_id='erd41', username=User_Management.objects.get(username='quang'), exam_id=Exam_Management.objects.get(exam_id='eswe201c'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd42', username=User_Management.objects.get(username='mai'), exam_id=Exam_Management.objects.get(exam_id='eswe201c'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd43', username=User_Management.objects.get(username='hoa'), exam_id=Exam_Management.objects.get(exam_id='eswe201c'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd44', username=User_Management.objects.get(username='nhan'), exam_id=Exam_Management.objects.get(exam_id='eswe201c'), state='offline')
#         Exam_Room_Doing.objects.create(erd_id='erd45', username=User_Management.objects.get(username='hieu'), exam_id=Exam_Management.objects.get(exam_id='eswe201c'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd46', username=User_Management.objects.get(username='linh'), exam_id=Exam_Management.objects.get(exam_id='eswe201c'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd47', username=User_Management.objects.get(username='thao'), exam_id=Exam_Management.objects.get(exam_id='eswe201c'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd48', username=User_Management.objects.get(username='chi'), exam_id=Exam_Management.objects.get(exam_id='eswe201c'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd49', username=User_Management.objects.get(username='dat'), exam_id=Exam_Management.objects.get(exam_id='eswe201c'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd50', username=User_Management.objects.get(username='an'), exam_id=Exam_Management.objects.get(exam_id='eswe201c'), state='online')
        
#         # emas1011
#         Exam_Room_Doing.objects.create(erd_id='erd51', username=User_Management.objects.get(username='hieu'), exam_id=Exam_Management.objects.get(exam_id='emas1011'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd52', username=User_Management.objects.get(username='hoa'), exam_id=Exam_Management.objects.get(exam_id='emas1011'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd53', username=User_Management.objects.get(username='thanh'), exam_id=Exam_Management.objects.get(exam_id='emas1011'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd54', username=User_Management.objects.get(username='mai'), exam_id=Exam_Management.objects.get(exam_id='emas1011'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd55', username=User_Management.objects.get(username='chi'), exam_id=Exam_Management.objects.get(exam_id='emas1011'), state='offline')
#         Exam_Room_Doing.objects.create(erd_id='erd56', username=User_Management.objects.get(username='linh'), exam_id=Exam_Management.objects.get(exam_id='emas1011'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd57', username=User_Management.objects.get(username='quang'), exam_id=Exam_Management.objects.get(exam_id='emas1011'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd58', username=User_Management.objects.get(username='minh'), exam_id=Exam_Management.objects.get(exam_id='emas1011'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd59', username=User_Management.objects.get(username='dat'), exam_id=Exam_Management.objects.get(exam_id='emas1011'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd60', username=User_Management.objects.get(username='an'), exam_id=Exam_Management.objects.get(exam_id='emas1011'), state='online')

#         # emai3911
#         Exam_Room_Doing.objects.create(erd_id='erd61', username=User_Management.objects.get(username='hoa'), exam_id=Exam_Management.objects.get(exam_id='emai3911'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd62', username=User_Management.objects.get(username='minh'), exam_id=Exam_Management.objects.get(exam_id='emai3911'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd63', username=User_Management.objects.get(username='an'), exam_id=Exam_Management.objects.get(exam_id='emai3911'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd64', username=User_Management.objects.get(username='huyen'), exam_id=Exam_Management.objects.get(exam_id='emai3911'), state='offline')
#         Exam_Room_Doing.objects.create(erd_id='erd65', username=User_Management.objects.get(username='quang'), exam_id=Exam_Management.objects.get(exam_id='emai3911'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd66', username=User_Management.objects.get(username='hieu'), exam_id=Exam_Management.objects.get(exam_id='emai3911'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd67', username=User_Management.objects.get(username='mai'), exam_id=Exam_Management.objects.get(exam_id='emai3911'), state='offline')
#         Exam_Room_Doing.objects.create(erd_id='erd68', username=User_Management.objects.get(username='linh'), exam_id=Exam_Management.objects.get(exam_id='emai3911'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd69', username=User_Management.objects.get(username='dat'), exam_id=Exam_Management.objects.get(exam_id='emai3911'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd70', username=User_Management.objects.get(username='nhan'), exam_id=Exam_Management.objects.get(exam_id='emai3911'), state='online')

#         # emai3912
#         Exam_Room_Doing.objects.create(erd_id='erd71', username=User_Management.objects.get(username='an'), exam_id=Exam_Management.objects.get(exam_id='emai3912'), state='offline')
#         Exam_Room_Doing.objects.create(erd_id='erd72', username=User_Management.objects.get(username='hoa'), exam_id=Exam_Management.objects.get(exam_id='emai3912'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd73', username=User_Management.objects.get(username='hieu'), exam_id=Exam_Management.objects.get(exam_id='emai3912'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd74', username=User_Management.objects.get(username='linh'), exam_id=Exam_Management.objects.get(exam_id='emai3912'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd75', username=User_Management.objects.get(username='minh'), exam_id=Exam_Management.objects.get(exam_id='emai3912'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd76', username=User_Management.objects.get(username='dat'), exam_id=Exam_Management.objects.get(exam_id='emai3912'), state='offline')
#         Exam_Room_Doing.objects.create(erd_id='erd77', username=User_Management.objects.get(username='mai'), exam_id=Exam_Management.objects.get(exam_id='emai3912'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd78', username=User_Management.objects.get(username='nhan'), exam_id=Exam_Management.objects.get(exam_id='emai3912'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd79', username=User_Management.objects.get(username='thanh'), exam_id=Exam_Management.objects.get(exam_id='emai3912'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd80', username=User_Management.objects.get(username='quang'), exam_id=Exam_Management.objects.get(exam_id='emai3912'), state='online')

#         # emas1012
#         Exam_Room_Doing.objects.create(erd_id='erd81', username=User_Management.objects.get(username='minh'), exam_id=Exam_Management.objects.get(exam_id='emas1012'), state='offline')
#         Exam_Room_Doing.objects.create(erd_id='erd82', username=User_Management.objects.get(username='huyen'), exam_id=Exam_Management.objects.get(exam_id='emas1012'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd83', username=User_Management.objects.get(username='hoa'), exam_id=Exam_Management.objects.get(exam_id='emas1012'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd84', username=User_Management.objects.get(username='chi'), exam_id=Exam_Management.objects.get(exam_id='emas1012'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd85', username=User_Management.objects.get(username='chi'), exam_id=Exam_Management.objects.get(exam_id='emas1012'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd86', username=User_Management.objects.get(username='linh'), exam_id=Exam_Management.objects.get(exam_id='emas1012'), state='offline')
#         Exam_Room_Doing.objects.create(erd_id='erd87', username=User_Management.objects.get(username='mai'), exam_id=Exam_Management.objects.get(exam_id='emas1012'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd88', username=User_Management.objects.get(username='quang'), exam_id=Exam_Management.objects.get(exam_id='emas1012'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd89', username=User_Management.objects.get(username='thanh'), exam_id=Exam_Management.objects.get(exam_id='emas1012'), state='online')
#         Exam_Room_Doing.objects.create(erd_id='erd90', username=User_Management.objects.get(username='dat'), exam_id=Exam_Management.objects.get(exam_id='emas1012'), state='online')

# # Add more here...


        
                
# # You can continue creating more entries in a similar manner
# # Create more entries as needed



#         # Insert data into History_Management model
#         # History_Management.objects.create(his_id='h1', erd_id=Exam_Room_Doing.objects.get(erd_id='erd1'), htime=parse_datetime('2023-12-23 15:01:00'), labels='normal')
#         # History_Management.objects.create(his_id='h2', erd_id=Exam_Room_Doing.objects.get(erd_id='erd1'), htime=parse_datetime('2023-12-23 15:30:00'), labels='abnormal')
#         # History_Management.objects.create(his_id='h3', erd_id=Exam_Room_Doing.objects.get(erd_id='erd2'), htime=parse_datetime('2023-12-23 15:15:45'), labels='normal')
#         # History_Management.objects.create(his_id='h4', erd_id=Exam_Room_Doing.objects.get(erd_id='erd3'), htime=parse_datetime('2023-12-23 15:17:45'), labels='normal')
#         # History_Management.objects.create(his_id='h5', erd_id=Exam_Room_Doing.objects.get(erd_id='erd1'), htime=parse_datetime('2023-12-23 15:20:45'), labels='normal')
#         # History_Management.objects.create(his_id='h6', erd_id=Exam_Room_Doing.objects.get(erd_id='erd7'), htime=parse_datetime('2023-12-26 09:25:30'), labels='abnormal')
#         # History_Management.objects.create(his_id='h7', erd_id=Exam_Room_Doing.objects.get(erd_id='erd2'), htime=parse_datetime('2023-12-23 15:46:30'), labels='normal')
#         # History_Management.objects.create(his_id='h8', erd_id=Exam_Room_Doing.objects.get(erd_id='erd2'), htime=parse_datetime('2023-12-23 15:48:30'), labels='abnormal')
#         # History_Management.objects.create(his_id='h9', erd_id=Exam_Room_Doing.objects.get(erd_id='erd3'), htime=parse_datetime('2023-12-23 15:48:30'), labels='abnormal')
#         # History_Management.objects.create(his_id='h10', erd_id=Exam_Room_Doing.objects.get(erd_id='erd7'), htime=parse_datetime('2023-12-26 09:40:30'), labels='abnormal')
#         # History_Management.objects.create(his_id='h11', erd_id=Exam_Room_Doing.objects.get(erd_id='erd7'), htime=parse_datetime('2023-12-26 09:20:30'), labels='normal')
#         # History_Management.objects.create(his_id='h12', erd_id=Exam_Room_Doing.objects.get(erd_id='erd7'), htime=parse_datetime('2023-12-26 09:50:30'), labels='abnormal')
#         # History_Management.objects.create(his_id='h13', erd_id=Exam_Room_Doing.objects.get(erd_id='erd9'), htime=parse_datetime('2023-12-26 16:15:30'), labels='abnormal')
#         # History_Management.objects.create(his_id='h14', erd_id=Exam_Room_Doing.objects.get(erd_id='erd9'), htime=parse_datetime('2023-12-26 16:20:30'), labels='normal')
#         # History_Management.objects.create(his_id='h15', erd_id=Exam_Room_Doing.objects.get(erd_id='erd9'), htime=parse_datetime('2023-12-26 16:25:30'), labels='abnormal')
        
        
 

# # Generate History Management entries without loops
#         History_Management.objects.create(his_id='h1', erd_id=Exam_Room_Doing.objects.get(erd_id='erd1'), htime=parse_datetime('2023-12-23 15:01:00'), labels='normal')
#         History_Management.objects.create(his_id='h2', erd_id=Exam_Room_Doing.objects.get(erd_id='erd1'), htime=parse_datetime('2023-12-23 15:15:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h3', erd_id=Exam_Room_Doing.objects.get(erd_id='erd2'), htime=parse_datetime('2023-12-23 15:05:00'), labels='normal')
#         History_Management.objects.create(his_id='h4', erd_id=Exam_Room_Doing.objects.get(erd_id='erd2'), htime=parse_datetime('2023-12-23 15:10:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h5', erd_id=Exam_Room_Doing.objects.get(erd_id='erd3'), htime=parse_datetime('2023-12-23 15:01:00'), labels='normal')
#         History_Management.objects.create(his_id='h6', erd_id=Exam_Room_Doing.objects.get(erd_id='erd3'), htime=parse_datetime('2023-12-23 15:10:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h7', erd_id=Exam_Room_Doing.objects.get(erd_id='erd4'), htime=parse_datetime('2023-12-23 15:08:00'), labels='normal')
#         History_Management.objects.create(his_id='h8', erd_id=Exam_Room_Doing.objects.get(erd_id='erd4'), htime=parse_datetime('2023-12-23 15:12:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h9', erd_id=Exam_Room_Doing.objects.get(erd_id='erd5'), htime=parse_datetime('2023-12-23 15:10:00'), labels='normal')
#         History_Management.objects.create(his_id='h10', erd_id=Exam_Room_Doing.objects.get(erd_id='erd5'), htime=parse_datetime('2023-12-23 15:15:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h11', erd_id=Exam_Room_Doing.objects.get(erd_id='erd6'), htime=parse_datetime('2023-12-23 15:07:00'), labels='normal')
#         History_Management.objects.create(his_id='h12', erd_id=Exam_Room_Doing.objects.get(erd_id='erd6'), htime=parse_datetime('2023-12-23 15:41:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h13', erd_id=Exam_Room_Doing.objects.get(erd_id='erd7'), htime=parse_datetime('2023-12-23 15:04:00'), labels='normal')
#         History_Management.objects.create(his_id='h14', erd_id=Exam_Room_Doing.objects.get(erd_id='erd7'), htime=parse_datetime('2023-12-23 15:23:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h15', erd_id=Exam_Room_Doing.objects.get(erd_id='erd8'), htime=parse_datetime('2023-12-23 15:02:00'), labels='normal')
#         History_Management.objects.create(his_id='h16', erd_id=Exam_Room_Doing.objects.get(erd_id='erd8'), htime=parse_datetime('2023-12-23 15:25:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h17', erd_id=Exam_Room_Doing.objects.get(erd_id='erd9'), htime=parse_datetime('2023-12-23 15:05:00'), labels='normal')
#         History_Management.objects.create(his_id='h18', erd_id=Exam_Room_Doing.objects.get(erd_id='erd9'), htime=parse_datetime('2023-12-23 15:25:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h19', erd_id=Exam_Room_Doing.objects.get(erd_id='erd10'), htime=parse_datetime('2023-12-23 15:02:00'), labels='normal')
#         History_Management.objects.create(his_id='h20', erd_id=Exam_Room_Doing.objects.get(erd_id='erd10'), htime=parse_datetime('2023-12-23 15:30:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h21', erd_id=Exam_Room_Doing.objects.get(erd_id='erd1'), htime=parse_datetime('2023-12-23 15:18:00'), labels='normal')
#         History_Management.objects.create(his_id='h22', erd_id=Exam_Room_Doing.objects.get(erd_id='erd1'), htime=parse_datetime('2023-12-23 15:29:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h23', erd_id=Exam_Room_Doing.objects.get(erd_id='erd2'), htime=parse_datetime('2023-12-23 15:15:00'), labels='normal')
#         History_Management.objects.create(his_id='h24', erd_id=Exam_Room_Doing.objects.get(erd_id='erd2'), htime=parse_datetime('2023-12-23 15:25:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h25', erd_id=Exam_Room_Doing.objects.get(erd_id='erd3'), htime=parse_datetime('2023-12-23 15:27:00'), labels='normal')
#         History_Management.objects.create(his_id='h26', erd_id=Exam_Room_Doing.objects.get(erd_id='erd3'), htime=parse_datetime('2023-12-23 15:45:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h27', erd_id=Exam_Room_Doing.objects.get(erd_id='erd4'), htime=parse_datetime('2023-12-23 15:40:00'), labels='normal')
#         History_Management.objects.create(his_id='h28', erd_id=Exam_Room_Doing.objects.get(erd_id='erd4'), htime=parse_datetime('2023-12-23 15:30:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h29', erd_id=Exam_Room_Doing.objects.get(erd_id='erd5'), htime=parse_datetime('2023-12-23 15:20:00'), labels='normal')
#         History_Management.objects.create(his_id='h30', erd_id=Exam_Room_Doing.objects.get(erd_id='erd5'), htime=parse_datetime('2023-12-23 15:25:00'), labels='abnormal')


#         History_Management.objects.create(his_id='h31', erd_id=Exam_Room_Doing.objects.get(erd_id='erd11'), htime=parse_datetime('2023-12-23 15:01:00'), labels='normal')
#         History_Management.objects.create(his_id='h32', erd_id=Exam_Room_Doing.objects.get(erd_id='erd11'), htime=parse_datetime('2023-12-23 15:15:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h33', erd_id=Exam_Room_Doing.objects.get(erd_id='erd12'), htime=parse_datetime('2023-12-23 15:05:00'), labels='normal')
#         History_Management.objects.create(his_id='h34', erd_id=Exam_Room_Doing.objects.get(erd_id='erd12'), htime=parse_datetime('2023-12-23 15:10:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h35', erd_id=Exam_Room_Doing.objects.get(erd_id='erd13'), htime=parse_datetime('2023-12-23 15:01:00'), labels='normal')
#         History_Management.objects.create(his_id='h36', erd_id=Exam_Room_Doing.objects.get(erd_id='erd13'), htime=parse_datetime('2023-12-23 15:10:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h37', erd_id=Exam_Room_Doing.objects.get(erd_id='erd14'), htime=parse_datetime('2023-12-23 15:08:00'), labels='normal')
#         History_Management.objects.create(his_id='h38', erd_id=Exam_Room_Doing.objects.get(erd_id='erd14'), htime=parse_datetime('2023-12-23 15:12:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h39', erd_id=Exam_Room_Doing.objects.get(erd_id='erd15'), htime=parse_datetime('2023-12-23 15:10:00'), labels='normal')
#         History_Management.objects.create(his_id='h40', erd_id=Exam_Room_Doing.objects.get(erd_id='erd15'), htime=parse_datetime('2023-12-23 15:15:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h41', erd_id=Exam_Room_Doing.objects.get(erd_id='erd16'), htime=parse_datetime('2023-12-23 15:07:00'), labels='normal')
#         History_Management.objects.create(his_id='h42', erd_id=Exam_Room_Doing.objects.get(erd_id='erd16'), htime=parse_datetime('2023-12-23 15:41:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h43', erd_id=Exam_Room_Doing.objects.get(erd_id='erd17'), htime=parse_datetime('2023-12-23 15:04:00'), labels='normal')
#         History_Management.objects.create(his_id='h44', erd_id=Exam_Room_Doing.objects.get(erd_id='erd17'), htime=parse_datetime('2023-12-23 15:23:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h45', erd_id=Exam_Room_Doing.objects.get(erd_id='erd18'), htime=parse_datetime('2023-12-23 15:02:00'), labels='normal')
#         History_Management.objects.create(his_id='h46', erd_id=Exam_Room_Doing.objects.get(erd_id='erd18'), htime=parse_datetime('2023-12-23 15:25:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h47', erd_id=Exam_Room_Doing.objects.get(erd_id='erd19'), htime=parse_datetime('2023-12-23 15:05:00'), labels='normal')
#         History_Management.objects.create(his_id='h48', erd_id=Exam_Room_Doing.objects.get(erd_id='erd19'), htime=parse_datetime('2023-12-23 15:25:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h49', erd_id=Exam_Room_Doing.objects.get(erd_id='erd20'), htime=parse_datetime('2023-12-23 15:02:00'), labels='normal')
#         History_Management.objects.create(his_id='h50', erd_id=Exam_Room_Doing.objects.get(erd_id='erd20'), htime=parse_datetime('2023-12-23 15:30:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h51', erd_id=Exam_Room_Doing.objects.get(erd_id='erd11'), htime=parse_datetime('2023-12-23 15:18:00'), labels='normal')
#         History_Management.objects.create(his_id='h52', erd_id=Exam_Room_Doing.objects.get(erd_id='erd11'), htime=parse_datetime('2023-12-23 15:29:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h53', erd_id=Exam_Room_Doing.objects.get(erd_id='erd12'), htime=parse_datetime('2023-12-23 15:15:00'), labels='normal')
#         History_Management.objects.create(his_id='h54', erd_id=Exam_Room_Doing.objects.get(erd_id='erd12'), htime=parse_datetime('2023-12-23 15:25:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h55', erd_id=Exam_Room_Doing.objects.get(erd_id='erd13'), htime=parse_datetime('2023-12-23 15:27:00'), labels='normal')
#         History_Management.objects.create(his_id='h56', erd_id=Exam_Room_Doing.objects.get(erd_id='erd13'), htime=parse_datetime('2023-12-23 15:45:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h57', erd_id=Exam_Room_Doing.objects.get(erd_id='erd14'), htime=parse_datetime('2023-12-23 15:40:00'), labels='normal')
#         History_Management.objects.create(his_id='h58', erd_id=Exam_Room_Doing.objects.get(erd_id='erd14'), htime=parse_datetime('2023-12-23 15:30:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h59', erd_id=Exam_Room_Doing.objects.get(erd_id='erd15'), htime=parse_datetime('2023-12-23 15:20:00'), labels='normal')
#         History_Management.objects.create(his_id='h60', erd_id=Exam_Room_Doing.objects.get(erd_id='erd15'), htime=parse_datetime('2023-12-23 15:25:00'), labels='abnormal')
        
        
#         History_Management.objects.create(his_id='h61', erd_id=Exam_Room_Doing.objects.get(erd_id='erd21'), htime=parse_datetime('2023-12-23 15:01:00'), labels='normal')
#         History_Management.objects.create(his_id='h62', erd_id=Exam_Room_Doing.objects.get(erd_id='erd21'), htime=parse_datetime('2023-12-23 15:15:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h63', erd_id=Exam_Room_Doing.objects.get(erd_id='erd22'), htime=parse_datetime('2023-12-23 15:05:00'), labels='normal')
#         History_Management.objects.create(his_id='h64', erd_id=Exam_Room_Doing.objects.get(erd_id='erd22'), htime=parse_datetime('2023-12-23 15:10:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h65', erd_id=Exam_Room_Doing.objects.get(erd_id='erd23'), htime=parse_datetime('2023-12-23 15:01:00'), labels='normal')
#         History_Management.objects.create(his_id='h66', erd_id=Exam_Room_Doing.objects.get(erd_id='erd23'), htime=parse_datetime('2023-12-23 15:10:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h67', erd_id=Exam_Room_Doing.objects.get(erd_id='erd24'), htime=parse_datetime('2023-12-23 15:08:00'), labels='normal')
#         History_Management.objects.create(his_id='h68', erd_id=Exam_Room_Doing.objects.get(erd_id='erd24'), htime=parse_datetime('2023-12-23 15:12:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h69', erd_id=Exam_Room_Doing.objects.get(erd_id='erd25'), htime=parse_datetime('2023-12-23 15:10:00'), labels='normal')
#         History_Management.objects.create(his_id='h70', erd_id=Exam_Room_Doing.objects.get(erd_id='erd25'), htime=parse_datetime('2023-12-23 15:15:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h71', erd_id=Exam_Room_Doing.objects.get(erd_id='erd26'), htime=parse_datetime('2023-12-23 15:07:00'), labels='normal')
#         History_Management.objects.create(his_id='h72', erd_id=Exam_Room_Doing.objects.get(erd_id='erd26'), htime=parse_datetime('2023-12-23 15:41:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h73', erd_id=Exam_Room_Doing.objects.get(erd_id='erd27'), htime=parse_datetime('2023-12-23 15:04:00'), labels='normal')
#         History_Management.objects.create(his_id='h74', erd_id=Exam_Room_Doing.objects.get(erd_id='erd27'), htime=parse_datetime('2023-12-23 15:23:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h75', erd_id=Exam_Room_Doing.objects.get(erd_id='erd28'), htime=parse_datetime('2023-12-23 15:02:00'), labels='normal')
#         History_Management.objects.create(his_id='h76', erd_id=Exam_Room_Doing.objects.get(erd_id='erd28'), htime=parse_datetime('2023-12-23 15:25:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h77', erd_id=Exam_Room_Doing.objects.get(erd_id='erd29'), htime=parse_datetime('2023-12-23 15:05:00'), labels='normal')
#         History_Management.objects.create(his_id='h78', erd_id=Exam_Room_Doing.objects.get(erd_id='erd29'), htime=parse_datetime('2023-12-23 15:25:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h79', erd_id=Exam_Room_Doing.objects.get(erd_id='erd30'), htime=parse_datetime('2023-12-23 15:02:00'), labels='normal')
#         History_Management.objects.create(his_id='h80', erd_id=Exam_Room_Doing.objects.get(erd_id='erd30'), htime=parse_datetime('2023-12-23 15:30:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h81', erd_id=Exam_Room_Doing.objects.get(erd_id='erd21'), htime=parse_datetime('2023-12-23 15:18:00'), labels='normal')
#         History_Management.objects.create(his_id='h82', erd_id=Exam_Room_Doing.objects.get(erd_id='erd21'), htime=parse_datetime('2023-12-23 15:29:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h83', erd_id=Exam_Room_Doing.objects.get(erd_id='erd22'), htime=parse_datetime('2023-12-23 15:15:00'), labels='normal')
#         History_Management.objects.create(his_id='h84', erd_id=Exam_Room_Doing.objects.get(erd_id='erd22'), htime=parse_datetime('2023-12-23 15:25:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h85', erd_id=Exam_Room_Doing.objects.get(erd_id='erd23'), htime=parse_datetime('2023-12-23 15:27:00'), labels='normal')
#         History_Management.objects.create(his_id='h86', erd_id=Exam_Room_Doing.objects.get(erd_id='erd23'), htime=parse_datetime('2023-12-23 15:45:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h87', erd_id=Exam_Room_Doing.objects.get(erd_id='erd24'), htime=parse_datetime('2023-12-23 15:40:00'), labels='normal')
#         History_Management.objects.create(his_id='h88', erd_id=Exam_Room_Doing.objects.get(erd_id='erd24'), htime=parse_datetime('2023-12-23 15:30:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h89', erd_id=Exam_Room_Doing.objects.get(erd_id='erd25'), htime=parse_datetime('2023-12-23 15:20:00'), labels='normal')
#         History_Management.objects.create(his_id='h90', erd_id=Exam_Room_Doing.objects.get(erd_id='erd25'), htime=parse_datetime('2023-12-23 15:25:00'), labels='abnormal')


#         History_Management.objects.create(his_id='h91', erd_id=Exam_Room_Doing.objects.get(erd_id='erd31'), htime=parse_datetime('2023-12-24 14:01:00'), labels='normal')
#         History_Management.objects.create(his_id='h92', erd_id=Exam_Room_Doing.objects.get(erd_id='erd31'), htime=parse_datetime('2023-12-24 14:25:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h93', erd_id=Exam_Room_Doing.objects.get(erd_id='erd32'), htime=parse_datetime('2023-12-24 14:10:00'), labels='normal')
#         History_Management.objects.create(his_id='h94', erd_id=Exam_Room_Doing.objects.get(erd_id='erd32'), htime=parse_datetime('2023-12-24 14:30:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h95', erd_id=Exam_Room_Doing.objects.get(erd_id='erd33'), htime=parse_datetime('2023-12-24 14:05:00'), labels='normal')
#         History_Management.objects.create(his_id='h96', erd_id=Exam_Room_Doing.objects.get(erd_id='erd33'), htime=parse_datetime('2023-12-24 14:20:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h97', erd_id=Exam_Room_Doing.objects.get(erd_id='erd34'), htime=parse_datetime('2023-12-24 14:08:00'), labels='normal')
#         History_Management.objects.create(his_id='h98', erd_id=Exam_Room_Doing.objects.get(erd_id='erd34'), htime=parse_datetime('2023-12-24 14:28:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h99', erd_id=Exam_Room_Doing.objects.get(erd_id='erd35'), htime=parse_datetime('2023-12-24 14:15:00'), labels='normal')
#         History_Management.objects.create(his_id='h100', erd_id=Exam_Room_Doing.objects.get(erd_id='erd35'), htime=parse_datetime('2023-12-24 14:29:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h101', erd_id=Exam_Room_Doing.objects.get(erd_id='erd36'), htime=parse_datetime('2023-12-24 14:07:00'), labels='normal')
#         History_Management.objects.create(his_id='h102', erd_id=Exam_Room_Doing.objects.get(erd_id='erd36'), htime=parse_datetime('2023-12-24 14:27:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h103', erd_id=Exam_Room_Doing.objects.get(erd_id='erd37'), htime=parse_datetime('2023-12-24 14:04:00'), labels='normal')
#         History_Management.objects.create(his_id='h104', erd_id=Exam_Room_Doing.objects.get(erd_id='erd37'), htime=parse_datetime('2023-12-24 14:22:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h105', erd_id=Exam_Room_Doing.objects.get(erd_id='erd38'), htime=parse_datetime('2023-12-24 14:02:00'), labels='normal')
#         History_Management.objects.create(his_id='h106', erd_id=Exam_Room_Doing.objects.get(erd_id='erd38'), htime=parse_datetime('2023-12-24 14:21:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h107', erd_id=Exam_Room_Doing.objects.get(erd_id='erd39'), htime=parse_datetime('2023-12-24 14:06:00'), labels='normal')
#         History_Management.objects.create(his_id='h108', erd_id=Exam_Room_Doing.objects.get(erd_id='erd39'), htime=parse_datetime('2023-12-24 14:23:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h109', erd_id=Exam_Room_Doing.objects.get(erd_id='erd40'), htime=parse_datetime('2023-12-24 14:03:00'), labels='normal')
#         History_Management.objects.create(his_id='h110', erd_id=Exam_Room_Doing.objects.get(erd_id='erd40'), htime=parse_datetime('2023-12-24 14:24:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h111', erd_id=Exam_Room_Doing.objects.get(erd_id='erd31'), htime=parse_datetime('2023-12-24 14:18:00'), labels='normal')
#         History_Management.objects.create(his_id='h112', erd_id=Exam_Room_Doing.objects.get(erd_id='erd31'), htime=parse_datetime('2023-12-24 14:26:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h113', erd_id=Exam_Room_Doing.objects.get(erd_id='erd32'), htime=parse_datetime('2023-12-24 14:14:00'), labels='normal')
#         History_Management.objects.create(his_id='h114', erd_id=Exam_Room_Doing.objects.get(erd_id='erd32'), htime=parse_datetime('2023-12-24 14:30:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h115', erd_id=Exam_Room_Doing.objects.get(erd_id='erd33'), htime=parse_datetime('2023-12-24 14:17:00'), labels='normal')
#         History_Management.objects.create(his_id='h116', erd_id=Exam_Room_Doing.objects.get(erd_id='erd33'), htime=parse_datetime('2023-12-24 14:28:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h117', erd_id=Exam_Room_Doing.objects.get(erd_id='erd34'), htime=parse_datetime('2023-12-24 14:10:00'), labels='normal')
#         History_Management.objects.create(his_id='h118', erd_id=Exam_Room_Doing.objects.get(erd_id='erd34'), htime=parse_datetime('2023-12-24 14:29:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h119', erd_id=Exam_Room_Doing.objects.get(erd_id='erd35'), htime=parse_datetime('2023-12-24 14:20:00'), labels='normal')
#         History_Management.objects.create(his_id='h120', erd_id=Exam_Room_Doing.objects.get(erd_id='erd35'), htime=parse_datetime('2023-12-24 14:27:00'), labels='abnormal')
        
#         # Create History Management objects for Exam Room Doings with erd_id from 41 to 50
#         History_Management.objects.create(his_id='h121', erd_id=Exam_Room_Doing.objects.get(erd_id='erd41'), htime=parse_datetime('2023-12-26 09:01:00'), labels='normal')
#         History_Management.objects.create(his_id='h122', erd_id=Exam_Room_Doing.objects.get(erd_id='erd41'), htime=parse_datetime('2023-12-26 09:17:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h123', erd_id=Exam_Room_Doing.objects.get(erd_id='erd42'), htime=parse_datetime('2023-12-26 09:07:00'), labels='normal')
#         History_Management.objects.create(his_id='h124', erd_id=Exam_Room_Doing.objects.get(erd_id='erd42'), htime=parse_datetime('2023-12-26 09:21:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h125', erd_id=Exam_Room_Doing.objects.get(erd_id='erd43'), htime=parse_datetime('2023-12-26 09:13:00'), labels='normal')
#         History_Management.objects.create(his_id='h126', erd_id=Exam_Room_Doing.objects.get(erd_id='erd43'), htime=parse_datetime('2023-12-26 09:28:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h127', erd_id=Exam_Room_Doing.objects.get(erd_id='erd44'), htime=parse_datetime('2023-12-26 09:04:00'), labels='normal')
#         History_Management.objects.create(his_id='h128', erd_id=Exam_Room_Doing.objects.get(erd_id='erd44'), htime=parse_datetime('2023-12-26 09:20:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h129', erd_id=Exam_Room_Doing.objects.get(erd_id='erd45'), htime=parse_datetime('2023-12-26 09:10:00'), labels='normal')
#         History_Management.objects.create(his_id='h130', erd_id=Exam_Room_Doing.objects.get(erd_id='erd45'), htime=parse_datetime('2023-12-26 09:24:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h131', erd_id=Exam_Room_Doing.objects.get(erd_id='erd46'), htime=parse_datetime('2023-12-26 09:15:00'), labels='normal')
#         History_Management.objects.create(his_id='h132', erd_id=Exam_Room_Doing.objects.get(erd_id='erd46'), htime=parse_datetime('2023-12-26 09:40:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h133', erd_id=Exam_Room_Doing.objects.get(erd_id='erd47'), htime=parse_datetime('2023-12-26 09:03:00'), labels='normal')
#         History_Management.objects.create(his_id='h134', erd_id=Exam_Room_Doing.objects.get(erd_id='erd47'), htime=parse_datetime('2023-12-26 09:22:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h135', erd_id=Exam_Room_Doing.objects.get(erd_id='erd48'), htime=parse_datetime('2023-12-26 09:02:00'), labels='normal')
#         History_Management.objects.create(his_id='h136', erd_id=Exam_Room_Doing.objects.get(erd_id='erd48'), htime=parse_datetime('2023-12-26 09:26:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h137', erd_id=Exam_Room_Doing.objects.get(erd_id='erd49'), htime=parse_datetime('2023-12-26 09:09:00'), labels='normal')
#         History_Management.objects.create(his_id='h138', erd_id=Exam_Room_Doing.objects.get(erd_id='erd49'), htime=parse_datetime('2023-12-26 09:30:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h139', erd_id=Exam_Room_Doing.objects.get(erd_id='erd50'), htime=parse_datetime('2023-12-26 09:05:00'), labels='normal')
#         History_Management.objects.create(his_id='h140', erd_id=Exam_Room_Doing.objects.get(erd_id='erd50'), htime=parse_datetime('2023-12-26 09:27:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h141', erd_id=Exam_Room_Doing.objects.get(erd_id='erd41'), htime=parse_datetime('2023-12-26 09:18:00'), labels='normal')
#         History_Management.objects.create(his_id='h142', erd_id=Exam_Room_Doing.objects.get(erd_id='erd41'), htime=parse_datetime('2023-12-26 09:29:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h143', erd_id=Exam_Room_Doing.objects.get(erd_id='erd42'), htime=parse_datetime('2023-12-26 09:15:00'), labels='normal')
#         History_Management.objects.create(his_id='h144', erd_id=Exam_Room_Doing.objects.get(erd_id='erd42'), htime=parse_datetime('2023-12-26 09:25:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h145', erd_id=Exam_Room_Doing.objects.get(erd_id='erd43'), htime=parse_datetime('2023-12-26 09:27:00'), labels='normal')
#         History_Management.objects.create(his_id='h146', erd_id=Exam_Room_Doing.objects.get(erd_id='erd43'), htime=parse_datetime('2023-12-26 09:45:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h147', erd_id=Exam_Room_Doing.objects.get(erd_id='erd44'), htime=parse_datetime('2023-12-26 09:40:00'), labels='normal')
#         History_Management.objects.create(his_id='h149', erd_id=Exam_Room_Doing.objects.get(erd_id='erd45'), htime=parse_datetime('2023-12-26 09:20:00'), labels='normal')
#         History_Management.objects.create(his_id='h150', erd_id=Exam_Room_Doing.objects.get(erd_id='erd45'), htime=parse_datetime('2023-12-26 09:35:00'), labels='abnormal')
        
#         History_Management.objects.create(his_id='h151', erd_id=Exam_Room_Doing.objects.get(erd_id='erd51'), htime=parse_datetime('2023-12-26 16:01:00'), labels='normal')
#         History_Management.objects.create(his_id='h152', erd_id=Exam_Room_Doing.objects.get(erd_id='erd51'), htime=parse_datetime('2023-12-26 16:20:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h153', erd_id=Exam_Room_Doing.objects.get(erd_id='erd52'), htime=parse_datetime('2023-12-26 16:05:00'), labels='normal')
#         History_Management.objects.create(his_id='h154', erd_id=Exam_Room_Doing.objects.get(erd_id='erd52'), htime=parse_datetime('2023-12-26 16:15:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h155', erd_id=Exam_Room_Doing.objects.get(erd_id='erd53'), htime=parse_datetime('2023-12-26 16:03:00'), labels='normal')
#         History_Management.objects.create(his_id='h156', erd_id=Exam_Room_Doing.objects.get(erd_id='erd53'), htime=parse_datetime('2023-12-26 16:25:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h157', erd_id=Exam_Room_Doing.objects.get(erd_id='erd54'), htime=parse_datetime('2023-12-26 16:08:00'), labels='normal')
#         History_Management.objects.create(his_id='h158', erd_id=Exam_Room_Doing.objects.get(erd_id='erd54'), htime=parse_datetime('2023-12-26 16:18:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h159', erd_id=Exam_Room_Doing.objects.get(erd_id='erd55'), htime=parse_datetime('2023-12-26 16:10:00'), labels='normal')
#         History_Management.objects.create(his_id='h160', erd_id=Exam_Room_Doing.objects.get(erd_id='erd55'), htime=parse_datetime('2023-12-26 16:30:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h161', erd_id=Exam_Room_Doing.objects.get(erd_id='erd56'), htime=parse_datetime('2023-12-26 16:12:00'), labels='normal')
#         History_Management.objects.create(his_id='h162', erd_id=Exam_Room_Doing.objects.get(erd_id='erd56'), htime=parse_datetime('2023-12-26 16:40:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h163', erd_id=Exam_Room_Doing.objects.get(erd_id='erd57'), htime=parse_datetime('2023-12-26 16:14:00'), labels='normal')
#         History_Management.objects.create(his_id='h164', erd_id=Exam_Room_Doing.objects.get(erd_id='erd57'), htime=parse_datetime('2023-12-26 16:38:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h165', erd_id=Exam_Room_Doing.objects.get(erd_id='erd58'), htime=parse_datetime('2023-12-26 16:16:00'), labels='normal')
#         History_Management.objects.create(his_id='h166', erd_id=Exam_Room_Doing.objects.get(erd_id='erd58'), htime=parse_datetime('2023-12-26 16:36:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h167', erd_id=Exam_Room_Doing.objects.get(erd_id='erd59'), htime=parse_datetime('2023-12-26 16:18:00'), labels='normal')
#         History_Management.objects.create(his_id='h168', erd_id=Exam_Room_Doing.objects.get(erd_id='erd59'), htime=parse_datetime('2023-12-26 16:34:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h169', erd_id=Exam_Room_Doing.objects.get(erd_id='erd60'), htime=parse_datetime('2023-12-26 16:20:00'), labels='normal')
#         History_Management.objects.create(his_id='h170', erd_id=Exam_Room_Doing.objects.get(erd_id='erd60'), htime=parse_datetime('2023-12-26 16:32:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h171', erd_id=Exam_Room_Doing.objects.get(erd_id='erd51'), htime=parse_datetime('2023-12-26 16:30:00'), labels='normal')
#         History_Management.objects.create(his_id='h172', erd_id=Exam_Room_Doing.objects.get(erd_id='erd51'), htime=parse_datetime('2023-12-26 16:28:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h173', erd_id=Exam_Room_Doing.objects.get(erd_id='erd52'), htime=parse_datetime('2023-12-26 16:40:00'), labels='normal')
#         History_Management.objects.create(his_id='h174', erd_id=Exam_Room_Doing.objects.get(erd_id='erd52'), htime=parse_datetime('2023-12-26 16:44:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h175', erd_id=Exam_Room_Doing.objects.get(erd_id='erd53'), htime=parse_datetime('2023-12-26 16:21:00'), labels='normal')
#         History_Management.objects.create(his_id='h176', erd_id=Exam_Room_Doing.objects.get(erd_id='erd53'), htime=parse_datetime('2023-12-26 16:25:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h177', erd_id=Exam_Room_Doing.objects.get(erd_id='erd54'), htime=parse_datetime('2023-12-26 16:29:00'), labels='normal')
#         History_Management.objects.create(his_id='h178', erd_id=Exam_Room_Doing.objects.get(erd_id='erd54'), htime=parse_datetime('2023-12-26 16:35:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h179', erd_id=Exam_Room_Doing.objects.get(erd_id='erd55'), htime=parse_datetime('2023-12-26 16:37:00'), labels='normal')
#         History_Management.objects.create(his_id='h180', erd_id=Exam_Room_Doing.objects.get(erd_id='erd55'), htime=parse_datetime('2023-12-26 16:42:00'), labels='abnormal')
        
#         History_Management.objects.create(his_id='h181', erd_id=Exam_Room_Doing.objects.get(erd_id='erd61'), htime=parse_datetime('2023-12-29 07:01:00'), labels='normal')
#         History_Management.objects.create(his_id='h182', erd_id=Exam_Room_Doing.objects.get(erd_id='erd61'), htime=parse_datetime('2023-12-29 07:30:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h183', erd_id=Exam_Room_Doing.objects.get(erd_id='erd62'), htime=parse_datetime('2023-12-29 07:15:00'), labels='normal')
#         History_Management.objects.create(his_id='h184', erd_id=Exam_Room_Doing.objects.get(erd_id='erd62'), htime=parse_datetime('2023-12-29 07:25:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h185', erd_id=Exam_Room_Doing.objects.get(erd_id='erd63'), htime=parse_datetime('2023-12-29 07:10:00'), labels='normal')
#         History_Management.objects.create(his_id='h186', erd_id=Exam_Room_Doing.objects.get(erd_id='erd63'), htime=parse_datetime('2023-12-29 07:20:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h187', erd_id=Exam_Room_Doing.objects.get(erd_id='erd64'), htime=parse_datetime('2023-12-29 07:05:00'), labels='normal')
#         History_Management.objects.create(his_id='h188', erd_id=Exam_Room_Doing.objects.get(erd_id='erd64'), htime=parse_datetime('2023-12-29 07:35:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h189', erd_id=Exam_Room_Doing.objects.get(erd_id='erd65'), htime=parse_datetime('2023-12-29 07:08:00'), labels='normal')
#         History_Management.objects.create(his_id='h190', erd_id=Exam_Room_Doing.objects.get(erd_id='erd65'), htime=parse_datetime('2023-12-29 07:27:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h191', erd_id=Exam_Room_Doing.objects.get(erd_id='erd66'), htime=parse_datetime('2023-12-29 07:03:00'), labels='normal')
#         History_Management.objects.create(his_id='h192', erd_id=Exam_Room_Doing.objects.get(erd_id='erd66'), htime=parse_datetime('2023-12-29 07:41:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h193', erd_id=Exam_Room_Doing.objects.get(erd_id='erd67'), htime=parse_datetime('2023-12-29 07:04:00'), labels='normal')
#         History_Management.objects.create(his_id='h194', erd_id=Exam_Room_Doing.objects.get(erd_id='erd67'), htime=parse_datetime('2023-12-29 07:23:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h195', erd_id=Exam_Room_Doing.objects.get(erd_id='erd68'), htime=parse_datetime('2023-12-29 07:02:00'), labels='normal')
#         History_Management.objects.create(his_id='h196', erd_id=Exam_Room_Doing.objects.get(erd_id='erd68'), htime=parse_datetime('2023-12-29 07:35:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h197', erd_id=Exam_Room_Doing.objects.get(erd_id='erd69'), htime=parse_datetime('2023-12-29 07:06:00'), labels='normal')
#         History_Management.objects.create(his_id='h198', erd_id=Exam_Room_Doing.objects.get(erd_id='erd69'), htime=parse_datetime('2023-12-29 07:29:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h199', erd_id=Exam_Room_Doing.objects.get(erd_id='erd70'), htime=parse_datetime('2023-12-29 07:08:00'), labels='normal')
#         History_Management.objects.create(his_id='h200', erd_id=Exam_Room_Doing.objects.get(erd_id='erd70'), htime=parse_datetime('2023-12-29 07:31:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h201', erd_id=Exam_Room_Doing.objects.get(erd_id='erd61'), htime=parse_datetime('2023-12-29 07:18:00'), labels='normal')
#         History_Management.objects.create(his_id='h202', erd_id=Exam_Room_Doing.objects.get(erd_id='erd61'), htime=parse_datetime('2023-12-29 07:29:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h203', erd_id=Exam_Room_Doing.objects.get(erd_id='erd62'), htime=parse_datetime('2023-12-29 07:15:00'), labels='normal')
#         History_Management.objects.create(his_id='h204', erd_id=Exam_Room_Doing.objects.get(erd_id='erd62'), htime=parse_datetime('2023-12-29 07:25:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h205', erd_id=Exam_Room_Doing.objects.get(erd_id='erd63'), htime=parse_datetime('2023-12-29 07:27:00'), labels='normal')
#         History_Management.objects.create(his_id='h206', erd_id=Exam_Room_Doing.objects.get(erd_id='erd63'), htime=parse_datetime('2023-12-29 07:45:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h207', erd_id=Exam_Room_Doing.objects.get(erd_id='erd64'), htime=parse_datetime('2023-12-29 07:40:00'), labels='normal')
#         History_Management.objects.create(his_id='h208', erd_id=Exam_Room_Doing.objects.get(erd_id='erd64'), htime=parse_datetime('2023-12-29 07:30:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h209', erd_id=Exam_Room_Doing.objects.get(erd_id='erd65'), htime=parse_datetime('2023-12-29 07:20:00'), labels='normal')
#         History_Management.objects.create(his_id='h210', erd_id=Exam_Room_Doing.objects.get(erd_id='erd65'), htime=parse_datetime('2023-12-29 07:25:00'), labels='abnormal')
        
#         History_Management.objects.create(his_id='h211', erd_id=Exam_Room_Doing.objects.get(erd_id='erd71'), htime=parse_datetime('2023-12-29 09:02:00'), labels='normal')
#         History_Management.objects.create(his_id='h212', erd_id=Exam_Room_Doing.objects.get(erd_id='erd71'), htime=parse_datetime('2023-12-29 09:25:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h213', erd_id=Exam_Room_Doing.objects.get(erd_id='erd72'), htime=parse_datetime('2023-12-29 09:07:00'), labels='normal')
#         History_Management.objects.create(his_id='h214', erd_id=Exam_Room_Doing.objects.get(erd_id='erd72'), htime=parse_datetime('2023-12-29 09:30:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h215', erd_id=Exam_Room_Doing.objects.get(erd_id='erd73'), htime=parse_datetime('2023-12-29 09:10:00'), labels='normal')
#         History_Management.objects.create(his_id='h216', erd_id=Exam_Room_Doing.objects.get(erd_id='erd73'), htime=parse_datetime('2023-12-29 09:35:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h217', erd_id=Exam_Room_Doing.objects.get(erd_id='erd74'), htime=parse_datetime('2023-12-29 09:15:00'), labels='normal')
#         History_Management.objects.create(his_id='h218', erd_id=Exam_Room_Doing.objects.get(erd_id='erd74'), htime=parse_datetime('2023-12-29 09:40:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h219', erd_id=Exam_Room_Doing.objects.get(erd_id='erd75'), htime=parse_datetime('2023-12-29 09:20:00'), labels='normal')
#         History_Management.objects.create(his_id='h220', erd_id=Exam_Room_Doing.objects.get(erd_id='erd75'), htime=parse_datetime('2023-12-29 09:45:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h221', erd_id=Exam_Room_Doing.objects.get(erd_id='erd76'), htime=parse_datetime('2023-12-29 09:22:00'), labels='normal')
#         History_Management.objects.create(his_id='h222', erd_id=Exam_Room_Doing.objects.get(erd_id='erd76'), htime=parse_datetime('2023-12-29 09:23:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h223', erd_id=Exam_Room_Doing.objects.get(erd_id='erd77'), htime=parse_datetime('2023-12-29 09:21:00'), labels='normal')
#         History_Management.objects.create(his_id='h224', erd_id=Exam_Room_Doing.objects.get(erd_id='erd77'), htime=parse_datetime('2023-12-29 09:11:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h225', erd_id=Exam_Room_Doing.objects.get(erd_id='erd78'), htime=parse_datetime('2023-12-29 09:32:00'), labels='normal')
#         History_Management.objects.create(his_id='h226', erd_id=Exam_Room_Doing.objects.get(erd_id='erd78'), htime=parse_datetime('2023-12-29 09:41:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h227', erd_id=Exam_Room_Doing.objects.get(erd_id='erd79'), htime=parse_datetime('2023-12-29 09:37:00'), labels='normal')
#         History_Management.objects.create(his_id='h228', erd_id=Exam_Room_Doing.objects.get(erd_id='erd79'), htime=parse_datetime('2023-12-29 09:40:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h229', erd_id=Exam_Room_Doing.objects.get(erd_id='erd80'), htime=parse_datetime('2023-12-29 09:42:00'), labels='normal')
#         History_Management.objects.create(his_id='h230', erd_id=Exam_Room_Doing.objects.get(erd_id='erd80'), htime=parse_datetime('2023-12-29 09:18:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h231', erd_id=Exam_Room_Doing.objects.get(erd_id='erd71'), htime=parse_datetime('2023-12-29 09:02:00'), labels='normal')
#         History_Management.objects.create(his_id='h232', erd_id=Exam_Room_Doing.objects.get(erd_id='erd71'), htime=parse_datetime('2023-12-29 09:25:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h233', erd_id=Exam_Room_Doing.objects.get(erd_id='erd72'), htime=parse_datetime('2023-12-29 09:07:00'), labels='normal')
#         History_Management.objects.create(his_id='h234', erd_id=Exam_Room_Doing.objects.get(erd_id='erd72'), htime=parse_datetime('2023-12-29 09:30:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h235', erd_id=Exam_Room_Doing.objects.get(erd_id='erd73'), htime=parse_datetime('2023-12-29 09:10:00'), labels='normal')
#         History_Management.objects.create(his_id='h236', erd_id=Exam_Room_Doing.objects.get(erd_id='erd73'), htime=parse_datetime('2023-12-29 09:35:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h237', erd_id=Exam_Room_Doing.objects.get(erd_id='erd74'), htime=parse_datetime('2023-12-29 09:15:00'), labels='normal')
#         History_Management.objects.create(his_id='h238', erd_id=Exam_Room_Doing.objects.get(erd_id='erd74'), htime=parse_datetime('2023-12-29 09:40:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h239', erd_id=Exam_Room_Doing.objects.get(erd_id='erd75'), htime=parse_datetime('2023-12-29 09:20:00'), labels='normal')
#         History_Management.objects.create(his_id='h240', erd_id=Exam_Room_Doing.objects.get(erd_id='erd75'), htime=parse_datetime('2023-12-29 09:45:00'), labels='abnormal')
        
#         History_Management.objects.create(his_id='h241', erd_id=Exam_Room_Doing.objects.get(erd_id='erd81'), htime=parse_datetime('2023-12-26 12:00:00'), labels='normal')
#         History_Management.objects.create(his_id='h242', erd_id=Exam_Room_Doing.objects.get(erd_id='erd81'), htime=parse_datetime('2023-12-26 12:20:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h243', erd_id=Exam_Room_Doing.objects.get(erd_id='erd82'), htime=parse_datetime('2023-12-26 12:05:00'), labels='normal')
#         History_Management.objects.create(his_id='h244', erd_id=Exam_Room_Doing.objects.get(erd_id='erd82'), htime=parse_datetime('2023-12-26 12:25:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h245', erd_id=Exam_Room_Doing.objects.get(erd_id='erd83'), htime=parse_datetime('2023-12-26 12:10:00'), labels='normal')
#         History_Management.objects.create(his_id='h246', erd_id=Exam_Room_Doing.objects.get(erd_id='erd83'), htime=parse_datetime('2023-12-26 12:30:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h247', erd_id=Exam_Room_Doing.objects.get(erd_id='erd84'), htime=parse_datetime('2023-12-26 12:15:00'), labels='normal')
#         History_Management.objects.create(his_id='h248', erd_id=Exam_Room_Doing.objects.get(erd_id='erd84'), htime=parse_datetime('2023-12-26 12:35:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h249', erd_id=Exam_Room_Doing.objects.get(erd_id='erd85'), htime=parse_datetime('2023-12-26 12:20:00'), labels='normal')
#         History_Management.objects.create(his_id='h250', erd_id=Exam_Room_Doing.objects.get(erd_id='erd85'), htime=parse_datetime('2023-12-26 12:40:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h251', erd_id=Exam_Room_Doing.objects.get(erd_id='erd86'), htime=parse_datetime('2023-12-26 12:25:00'), labels='normal')
#         History_Management.objects.create(his_id='h252', erd_id=Exam_Room_Doing.objects.get(erd_id='erd86'), htime=parse_datetime('2023-12-26 12:45:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h253', erd_id=Exam_Room_Doing.objects.get(erd_id='erd87'), htime=parse_datetime('2023-12-26 12:30:00'), labels='normal')
#         History_Management.objects.create(his_id='h254', erd_id=Exam_Room_Doing.objects.get(erd_id='erd87'), htime=parse_datetime('2023-12-26 12:50:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h255', erd_id=Exam_Room_Doing.objects.get(erd_id='erd88'), htime=parse_datetime('2023-12-26 12:35:00'), labels='normal')
#         History_Management.objects.create(his_id='h256', erd_id=Exam_Room_Doing.objects.get(erd_id='erd88'), htime=parse_datetime('2023-12-26 12:55:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h257', erd_id=Exam_Room_Doing.objects.get(erd_id='erd89'), htime=parse_datetime('2023-12-26 12:40:00'), labels='normal')
#         History_Management.objects.create(his_id='h258', erd_id=Exam_Room_Doing.objects.get(erd_id='erd89'), htime=parse_datetime('2023-12-26 12:59:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h259', erd_id=Exam_Room_Doing.objects.get(erd_id='erd90'), htime=parse_datetime('2023-12-26 12:45:00'), labels='normal')
#         History_Management.objects.create(his_id='h261', erd_id=Exam_Room_Doing.objects.get(erd_id='erd87'), htime=parse_datetime('2023-12-26 12:00:00'), labels='normal')
#         History_Management.objects.create(his_id='h262', erd_id=Exam_Room_Doing.objects.get(erd_id='erd87'), htime=parse_datetime('2023-12-26 12:15:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h263', erd_id=Exam_Room_Doing.objects.get(erd_id='erd88'), htime=parse_datetime('2023-12-26 12:20:00'), labels='normal')
#         History_Management.objects.create(his_id='h264', erd_id=Exam_Room_Doing.objects.get(erd_id='erd88'), htime=parse_datetime('2023-12-26 12:30:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h265', erd_id=Exam_Room_Doing.objects.get(erd_id='erd89'), htime=parse_datetime('2023-12-26 12:35:00'), labels='normal')
#         History_Management.objects.create(his_id='h266', erd_id=Exam_Room_Doing.objects.get(erd_id='erd89'), htime=parse_datetime('2023-12-26 12:45:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h267', erd_id=Exam_Room_Doing.objects.get(erd_id='erd81'), htime=parse_datetime('2023-12-26 12:15:00'), labels='normal')
#         History_Management.objects.create(his_id='h268', erd_id=Exam_Room_Doing.objects.get(erd_id='erd84'), htime=parse_datetime('2023-12-26 12:13:00'), labels='abnormal')
#         History_Management.objects.create(his_id='h269', erd_id=Exam_Room_Doing.objects.get(erd_id='erd82'), htime=parse_datetime('2023-12-26 12:17:00'), labels='normal')
#         History_Management.objects.create(his_id='h270', erd_id=Exam_Room_Doing.objects.get(erd_id='erd85'), htime=parse_datetime('2023-12-26 12:42:00'), labels='abnormal')


        

        
        

        
        


        




#         self.stdout.write(self.style.SUCCESS('Data inserted successfully!'))




