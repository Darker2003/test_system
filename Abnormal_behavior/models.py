from django.db import models

# Create your models here.
class User_Management(models.Model):
    username = models.CharField(max_length=15, primary_key=True, db_index=True)
    upassword = models.CharField(max_length=30, null=False)
    utype = models.CharField(max_length=10, default='normal', choices=[('normal', 'Normal'), ('vip', 'VIP')], null=False)
    remainday = models.IntegerField(null=False)
    ucode = models.CharField(max_length=10, null=False)
    mail = models.EmailField(null=False)
    phone = models.CharField(max_length=15, null=False)

class Bill(models.Model):
    bill_id = models.CharField(max_length=15, primary_key=True, db_index=True)
    username = models.ForeignKey(User_Management, on_delete=models.CASCADE)
    bill_date = models.DateTimeField(null=False)

class Exam_Management(models.Model):
    exam_id = models.CharField(max_length=15, primary_key=True, db_index=True)
    course_id = models.CharField(max_length=15, null=False, db_index=True)
    exam_date = models.DateTimeField(null=False)
    duration = models.PositiveIntegerField(null=False)
    room_id = models.CharField(max_length=15, null=False)
    supervisor = models.ForeignKey(User_Management, on_delete=models.CASCADE)
    

class Exam_Room_Doing(models.Model):
    erd_id = models.CharField(max_length=10, primary_key=True, db_index=True)
    username = models.ForeignKey(User_Management, on_delete=models.CASCADE)
    exam_id = models.ForeignKey(Exam_Management, on_delete=models.CASCADE)
    state = models.CharField(max_length=10, default='online', choices=[('online', 'Online'), ('offline', 'Offline')], null=False)
    
    def save(self, *args, **kwargs):
        if not self.erd_id:
            last_instance = Exam_Room_Doing.objects.last()
            last_number = int(last_instance.erd_id[3:]) if last_instance else 0
            self.erd_id = f'erd{last_number + 1}'
        super().save(*args, **kwargs)

class History_Management(models.Model):
    his_id = models.CharField(max_length=10, primary_key=True, db_index=True)
    erd_id = models.ForeignKey(Exam_Room_Doing, on_delete=models.CASCADE)
    htime = models.DateTimeField(null=False)
    labels = models.CharField(max_length=10, default='normal', choices=[('normal', 'Normal'), ('abnormal', 'Abnormal')])
    state = models.CharField(max_length=10, default='0', choices=[('0', '0'), ('1', '1')])
    def save(self, *args, **kwargs):
        if not self.his_id:
            last_instance = History_Management.objects.last()
            last_number = int(last_instance.his_id[1:]) if last_instance else 0
            self.his_id = f'h{last_number + 1}'
        super().save(*args, **kwargs)

class Quotes(models.Model):
    qid = models.AutoField(primary_key = True)
    qmail = models.EmailField(null=False)
    qname = models.CharField(max_length=100, null=False)
    qphone = models.CharField(max_length=15, null=False)
    qadvise = models.CharField(max_length=10, choices=[('Exam', 'Exam'), ('Tool', 'Tool')], null=False)
    qmessage = models.TextField(null=False)
    
class Services(models.Model):
    ser_id = models.CharField(max_length=10, primary_key=True, db_index=True)
    service_type = models.CharField(max_length=10, default='Exam', choices=[('Exam', 'Exam'), ('Tool', 'Tool')], null=False)

class User_Services(models.Model):
    user_id = models.CharField(max_length=10, primary_key=True, db_index=True)
    username = models.ForeignKey(User_Management, on_delete=models.CASCADE)
    service_type = models.ForeignKey(Services, on_delete=models.CASCADE)

class Services_Price(models.Model):
    sp_id = models.CharField(max_length=10, primary_key=True, db_index=True)
    service_type = models.ForeignKey(Services, on_delete=models.CASCADE)
    price = models.IntegerField(null=False)
    duration = models.IntegerField(null=False)


class IP_state(models.Model):
    id = models.AutoField(primary_key=True)
    IP = models.CharField(max_length=20)
    erd_id = models.ForeignKey(Exam_Room_Doing, on_delete=models.CASCADE)
    time = models.DateTimeField(null=False)
    state = models.CharField(max_length=10, default='online', choices=[('offline','Offline'),('online','Online')])
    
class Quiz(models.Model):
    exam_id = models.CharField(max_length=100)
    course_id = models.CharField(max_length=100)
    json_data = models.JSONField()

class Save_Quiz(models.Model):
    exam_id = models.CharField(max_length=100)
    json_data = models.JSONField()