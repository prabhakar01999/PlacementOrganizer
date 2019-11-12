from django.db import models
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.timezone import now

class StudentProfile(models.Model):
    hallTicketNumber = models.CharField(max_length=15, primary_key=True)
    firstName = models.CharField(max_length=25)
    middleName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    GENDER_CHOICES = (('Male', 'Male'),('Female','Female'),('Other','Other'),)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='Male')
    dateOfBirth = models.DateField()
    fatherGuardianName = models.CharField(max_length=100)
    fatherGuardianOccupation = models.CharField(max_length=30)
    fatherGuardianDesignation = models.CharField(max_length=30)
    fatherGuardianAnnualIncome = models.IntegerField(default=0)
    motherName = models.CharField(max_length=100)
    motherOccupation = models.CharField(max_length=30)
    motherDesignation = models.CharField(max_length=30)
    motherAnnualIncome = models.IntegerField(default=0)
    primaryEmail = models.EmailField()
    alternateEmail = models.EmailField()
    primaryPhoneNumber = models.CharField(max_length=10)
    alternatePhoneNumber = models.CharField(max_length=10)
    parentEmail = models.EmailField()
    fatherGuardianPhoneNumber = models.CharField(max_length=10)
    motherPhoneNumber = models.CharField(max_length=10)
    landline = models.CharField(max_length=8)
    aadharNumber = models.CharField(max_length=12)
    panNumber = models.CharField(max_length = 10)
    passportNumber = models.CharField(max_length = 8)
    presentAddress = models.TextField(max_length=255)
    permanentAddress = models.TextField(max_length=255)
    TENTH_BOARD_CHOICES =(('SSC','SSC'),('CBSE','CBSE'),('ICSE','ICSE'),('others','others'))
    tenthBoard = models.CharField(max_length=6, choices=TENTH_BOARD_CHOICES, default='SSC')
    tenthYearOfPassing = models.CharField(max_length=4)
    schoolName = models.CharField(max_length = 50)
    tenthGpa = models.DecimalField(max_digits=3, decimal_places=2)
    INTER_BOARD_CHOICES =(('BIE','BIE'),('CBSE','CBSE'),('ICSE','ICSE'),('others','others'))
    interBoard = models.CharField(max_length=6, choices=TENTH_BOARD_CHOICES, default='SSC')
    interYearOfPassing = models.CharField(max_length=4)
    collegeName = models.CharField(max_length = 50)
    interPercentage = models.DecimalField(max_digits=3, decimal_places=1)
    engineeringYearOfPassing = models.CharField(max_length=4)
    emcetRank = models.IntegerField()
    CATEGORY_CHOICES = (('OC','OC'),('BC','BC'),('OBC','OBC'),('EBC','EBC'),('SC','SC'),('ST','ST'),('PH','PH'),('CAP','CAP'))
    category = models.CharField(max_length = 3, choices = CATEGORY_CHOICES, default='OC')
    ADMISSION_CHOICES = (('Convener','Convener'),('B-Category','B-Category'),('Spot Admission','Spot Admission'),('Other','Other'))
    BRANCH_CHOICES = (('CIVIL','CIVIL'),('CSE','CSE'),('ECE','ECE'),('EEE','EEE'),('IT','IT'),('MECH','MECH'))
    admissionType = models.CharField(max_length=15, choices=ADMISSION_CHOICES, default='Convener')
    branch = models.CharField(max_length=5, choices=BRANCH_CHOICES)
    sem1GPA = models.DecimalField(max_digits=3, decimal_places=2)
    sem2GPA = models.DecimalField(max_digits=3, decimal_places=2)
    sem3GPA = models.DecimalField(max_digits=3, decimal_places=2)
    sem4GPA = models.DecimalField(max_digits=3, decimal_places=2)
    sem5GPA = models.DecimalField(max_digits=3, decimal_places=2)
    sem6GPA = models.DecimalField(max_digits=3, decimal_places=2)
    sem7GPA = models.DecimalField(max_digits=3, decimal_places=2)
    sem8GPA = models.DecimalField(max_digits=3, decimal_places=2)
    CGPA = models.DecimalField(max_digits=3, decimal_places=2)
    BACKLOG_CHOICES = (('Yes','Yes'),('No','No'))
    SEVENTH_AND_EIGHTH_SEM_CHOICES=(('completed','completed'),('stillBacklog','stillBacklog'),('not-yet','not-yet'))
    SEM_STATUS_CHOICES = (('completed','completed'),('stillBacklog','stillBacklog'))
    backlogs = models.CharField(max_length = 3, choices = BACKLOG_CHOICES, default = 'No')
    sem1backlog = models.CharField(max_length=3, choices = BACKLOG_CHOICES, default = 'No')
    sem1Completed = models.CharField(max_length=9, choices = SEM_STATUS_CHOICES, default = 'Yes')
    sem2backlog = models.CharField(max_length=3, choices = BACKLOG_CHOICES, default = 'No')
    sem2Completed = models.CharField(max_length=9, choices = SEM_STATUS_CHOICES, default = 'Yes')
    sem3backlog = models.CharField(max_length=3, choices = BACKLOG_CHOICES, default = 'No')
    sem3Completed = models.CharField(max_length=9, choices = SEM_STATUS_CHOICES, default = 'Yes')
    sem4backlog = models.CharField(max_length=3, choices = BACKLOG_CHOICES, default = 'No')
    sem4Completed = models.CharField(max_length=9, choices = SEM_STATUS_CHOICES, default = 'Yes')
    sem5backlog = models.CharField(max_length=3, choices = BACKLOG_CHOICES, default = 'No')
    sem5Completed = models.CharField(max_length=9, choices = SEM_STATUS_CHOICES, default = 'Yes')
    sem6backlog = models.CharField(max_length=3, choices = BACKLOG_CHOICES, default = 'No') 
    sem6Completed = models.CharField(max_length=9, choices = SEM_STATUS_CHOICES, default = 'Yes')
    sem7backlog = models.CharField(max_length=3, choices = BACKLOG_CHOICES, default = 'No')
    sem7Completed = models.CharField(max_length=12, choices = SEVENTH_AND_EIGHTH_SEM_CHOICES, default = 'No')
    sem8backlog = models.CharField(max_length=3, choices = BACKLOG_CHOICES, default = 'No')
    sem8Completed = models.CharField(max_length=12, choices = SEVENTH_AND_EIGHTH_SEM_CHOICES, default = 'No')
    presentBacklogs = models.IntegerField(default = 0)
    sem1Memo = models.FileField()
    sem2Memo = models.FileField()
    sem3Memo = models.FileField()
    sem4Memo = models.FileField()
    sem5Memo = models.FileField()
    sem6Memo = models.FileField()
    sem7Memo = models.FileField()
    sem8Memo = models.FileField()
    def __str__(self):
        return self.hallTicketNumber
class Certificates(models.Model):
    certificateName = models.FileField()
    certificateDescription = models.CharField(max_length=50, default="")
    student = models.ForeignKey(StudentProfile, on_delete = models.CASCADE, related_name="certificates")
    def __str__(self):
        return self.student.hallTicketNumber


def current_year():
        return datetime.date.today().year

def max_value_current_year(value):
        return MaxValueValidator(current_year())(value)
        
class Placed(models.Model):
    def current_year():
        return datetime.date.today().year

    def max_value_current_year(value):
        return MaxValueValidator(current_year())(value)
        
    companyName = models.CharField(max_length = 50)
    payPackage = models.DecimalField(max_digits=5, decimal_places=2)
    year = models.PositiveIntegerField(default=current_year(), validators=[MinValueValidator(1984), max_value_current_year])
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name="placements")
    def __str__(self):
        return self.student.hallTicketNumber


    
class Company(models.Model):
    companyName = models.CharField(max_length=50)
    companyEmail = models.CharField(max_length=50)
    exam_date = models.DateField()
    eligibleStudents = models.FileField()
    def __str__(self):
        return self.companyName


class QuestionBank(models.Model):
    student = models.ForeignKey(StudentProfile, related_name="questions", on_delete=models.CASCADE)
    company = models.ForeignKey(Company, related_name="companies", on_delete = models.CASCADE)
    date  = models.DateField(default = datetime.date.today())
    round_no = models.PositiveIntegerField(default = 1)
    questions = models.TextField(max_length = 1500)
    def __str__(self):
        return self.company.companyName+' '+str(self.round_no)+str(self.student.hallTicketNumber)