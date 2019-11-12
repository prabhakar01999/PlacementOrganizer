from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentProfile, Certificates, QuestionBank, Company


def placementform(request):
    return render(request,'student/placement-form.html')

def form(request):
    return render(request,'student/form.html')

def bank(request):
    return render(request,'student/bank.html')
def submit_successful(request):
    return render(request,'student/submit_successful.html')
    
def createStudent(request):
    if request.method == 'POST':
        if request.POST['hallTicketNo'] and request.POST['firstName'] and request.POST['lastName'] and request.POST['gender'] and request.POST['dob'] and request.POST['fatherOrGuardianName'] and request.POST['fatherOrGuardianOccupation'] and request.POST['motherName'] and request.POST['motherOccupation'] and request.POST['studentPrimaryEmail'] and  request.POST['studentPrimaryNumber'] and request.POST['fatherOrGuardianNumber'] and request.POST['motherNumber'] and request.POST['presentAddress'] and request.POST['permanentAddress'] and request.POST['10thBoard'] and request.POST['10thyop'] and request.POST['school'] and request.POST['10thgpa'] and request.POST['inter-Board'] and request.POST['inter-yop'] and request.POST['college'] and request.POST['inter-percentage'] and request.POST['engineering-yop'] and request.POST['eamcet-rank'] and request.POST['category'] and request.POST['typeOfAdmission'] and request.POST['branch'] and request.POST['1semGrade'] and request.POST['2semGrade'] and request.POST['3semGrade'] and request.POST['4semGrade'] and request.POST['5semGrade'] and request.POST['cgpa'] and request.POST['BacklogHistory'] and request.POST['1semBacklogHistory'] and request.POST['2semBacklogHistory'] and request.POST['3semBacklogHistory'] and request.POST['4semBacklogHistory'] and request.POST['5semBacklogHistory'] and request.POST['6semBacklogHistory'] and request.POST['1semMemo'] and request.POST['2semMemo'] and request.POST['3semMemo'] and request.POST['4semMemo'] and request.POST['5semMemo'] :
            profile = StudentProfile()
            profile.hallTicketNumber = request.POST['hallTicketNo']
            profile.firstName = request.POST['firstName']
            profile.middleName = request.POST['middleName']
            profile.lastName = request.POST['lastName'] 
            profile.gender = request.POST['gender']
            profile.dateOfBirth = request.POST['dob']
            profile.fatherGuardianName = request.POST['fatherOrGuardianName']
            profile.fatherGuardianOccupation = request.POST['fatherOrGuardianOccupation']
            profile.fatherGuardianDesignation = request.POST['fatherOrGuardianDesignation']
            profile.fatherGuardianAnnualIncome =request.POST['fatherOrGuardianAnnualIncome']
            profile.motherName = request.POST['motherName']
            profile.motherOccupation = request.POST['motherOccupation']
            profile.motherDesignation = request.POST['motherDesignation']
            profile.motherAnnualIncome = request.POST['motherAnnualIncome']
            profile.primaryEmail = request.POST['studentPrimaryEmail']
            profile.alternateEmail = request.POST['studentAlternateEmail']
            profile.parentEmail = request.POST['parentEmail']
            profile.primaryPhoneNumber = request.POST['studentPrimaryNumber']
            profile.alternatePhoneNumber = request.POST['studentAlternateNumber']
            profile.fatherGuardianPhoneNumber = request.POST['fatherOrGuardianNumber']
            profile.motherPhoneNumber = request.POST['motherNumber']
            profile.landline = request.POST['landLine']
            profile.aadharNumber = request.POST['aadharNumber']
            profile.panNumber = request.POST['panNumber']
            profile.passportNumber = request.POST['passportNumber']
            profile.presentAddress = request.POST['presentAddress']
            profile.permanentAddress = request.POST['permanentAddress']
            profile.tenthBoard = request.POST['10thBoard']
            profile.tenthYearOfPassing = request.POST['10thyop']
            profile.schoolName = request.POST['school']
            profile.tenthGpa = request.POST['10thgpa']
            profile.interBoard = request.POST['inter-Board']
            profile.interYearOfPassing = request.POST['inter-yop']
            profile.collegeName = request.POST['college']
            profile.interPercentage = request.POST['inter-percentage']
            profile.engineeringYearOfPassing = request.POST['engineering-yop']
            profile.emcetRank = request.POST['eamcet-rank']
            profile.category = request.POST['category']
            profile.admissionType = request.POST['typeOfAdmission']
            profile.branch = request.POST['branch']
            profile.sem1GPA = request.POST['1semGrade']
            profile.sem2GPA = request.POST['2semGrade']
            profile.sem3GPA = request.POST['3semGrade']
            profile.sem4GPA = request.POST['4semGrade']
            profile.sem5GPA = request.POST['5semGrade']
            profile.sem6GPA = request.POST['6semGrade']
            profile.sem7GPA = request.POST['7semGrade']
            profile.sem8GPA = request.POST['8semGrade']
            profile.CGPA = request.POST['cgpa']
            profile.backlogs = request.POST['BacklogHistory']
            profile.sem1backlog = request.POST['1semBacklogHistory']
            profile.sem1Completed = request.POST['1semStatus']
            profile.sem2backlog = request.POST['2semBacklogHistory']
            profile.sem2Completed = request.POST['2semStatus']
            profile.sem3backlog = request.POST['3semBacklogHistory']
            profile.sem3Completed = request.POST['3semStatus']
            profile.sem4backlog = request.POST['4semBacklogHistory']
            profile.sem4Completed = request.POST['4semStatus']
            profile.sem5backlog = request.POST['5semBacklogHistory']
            profile.sem5Completed = request.POST['5semStatus']
            profile.sem6backlog = request.POST['6semBacklogHistory']
            profile.sem6Completed = request.POST['6semStatus']
            profile.sem7backlog = request.POST['7semBacklogHistory']
            profile.sem7Completed = request.POST['7semStatus']
            profile.sem8backlog = request.POST['8semBacklogHistory']
            profile.sem8Completed = request.POST['8semStatus']
            profile.presentBacklogs = request.POST['presentBacklogs']
            profile.sem1Memo = request.POST['1semMemo']
            profile.sem2Memo = request.POST['2semMemo']
            profile.sem3Memo = request.POST['3semMemo']
            profile.sem4Memo = request.POST['4semMemo']
            profile.sem5Memo = request.POST['5semMemo']
            profile.sem6Memo = request.POST['6semMemo']
            profile.sem7Memo = request.POST['7semMemo']
            profile.sem8Memo = request.POST['8semMemo']
            profile.languages = request.POST.getlist('language')
            profile.save()
            n = request.POST['noOfCertificates']
            n =int(n)
            for i in range(1,n+1):
                certificate = Certificates()
                name = 'Certificate'+ str(i)
                description = name+"description"
                certificate.certificateName = request.POST[name]
                certificate.certificateDescription = request.POST[description]
                certificate.student = profile
                certificate.save()
            return render(request, 'student/submit_successful.html')

        else:
            return render(request, 'student/placement-form.html', {'error':'Please fill the required fields'})

    else:
        return render(request, 'student/placement-form.html')

def questionBank(request):
    return render(request, 'student/questionBank.html')


def storeQuestionBank(request):
    if request.method == 'POST':
        if request.POST['hallTicketNumber'] and request.POST['company'] and request.POST['date'] and request.POST['round'] and request.POST['questions']:
            qBank = QuestionBank()
            try:
                qBank.student=StudentProfile.objects.get(hallTicketNumber = request.POST['hallTicketNumber'])
            except:
                return render(request, 'student/bank.html',{'error':'Please enter correct hall ticket number'})
            try:
                qBank.company = Company.objects.get(companyName = request.POST['company'])
            except:
                return render(request, 'student/bank.html',{'error':'Please choose correct company name'})
            qBank.date = request.POST['date']
            qBank.round_no = request.POST['round']
            qBank.questions = request.POST['questions']
            qBank.save()
            return render(request, 'student/submit_successful.html')
        else:
            return render(request, 'student/questionBank.html',{'error':'Please fill the required fields'})

    else:
        return render(request, 'student/questionBank')



            
