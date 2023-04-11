from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f"{self.name} 전문의"

class Patient(models.Model):
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    # doctors = models.ManyToManyField(Doctor, related_name='patients')
    doctors = models.ManyToManyField(Doctor, through='Reservation')
    name = models.TextField()

    def __str__(self):
        return f"{self.pk}번 환자 {self.name}"
    
# # 관계를 기억해주는 중개모델 생성
# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.doctor_id}번 의사의 {self.patient_id}번 환자"


# 정보 있는데 모델 수정 시 DB 삭제, 마이그레이션 삭제 후 진행

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.doctor.pk}번 의사의 {self.patient.pk}번 환자"