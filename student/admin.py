from django.contrib import admin
from .models import StudentProfile, Certificates, Placed, Company, QuestionBank
from advanced_filters.admin import AdminAdvancedFiltersMixin
import csv
from io import StringIO
from django.http import HttpResponse, FileResponse
from django.core.mail import send_mail, EmailMessage
admin.site.site_header="Vasavi Placement Organizer"
class StudentProfileAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    
    def downloadCSV(self, request, queryset):
        f = StringIO()
        writer = csv.writer(f)
        writer.writerow(['Hallticket Number', 'First Name', 'Middle Name', 'Last Name', 'Gender', 'Primary Email', 'Alternate Email', 'Primary Phone Nummber', 'Alternate Phone Number', 'CGPA', 'No. of Backlogs'])
        for i in queryset:
            writer.writerow([i.hallTicketNumber, i.firstName, i.middleName, i.lastName, i.gender, i.primaryEmail, i.alternateEmail, i.primaryPhoneNumber, i.alternatePhoneNumber, i.CGPA, i.presentBacklogs])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename = filtered-student-list.csv'
        return response

    downloadCSV.short_description = "Download list in csv format"

    actions = ['downloadCSV']
    advanced_filter_fields = (
        'gender',
        'branch',
        'CGPA',
        'presentBacklogs',
        ('placements__companyName', 'companies allowed'),
    )


class CompanyFilterAdmin(admin.ModelAdmin):
    def mailCompany(self, request, queryset):
        subject = 'List of eligible candidates from Vasavi College Of Engineering'
        content = 'Please find the list of eligible students for your organization in the attached.'
        from_address = 'placementcellvasavi@gmail.com'
        for i in queryset:
            email_address = []
            email_address.append(i.companyEmail)
            mail = EmailMessage(subject, content, from_address, email_address)
            attachment = i.eligibleStudents
            mail.attach(attachment.name, attachment.read(), 'text/csv')
            mail.send()

    def mailStudents(self, request, queryset):
        for i in queryset:
            subject = i.companyName+"'s exam on "+i.examDate
            content = "You are eligible to attend the exam conducted by "+i.companyName+" on "+str(i.examDate)+" for round "+str(i.round_no)+" please enter the questions asked in the link -> localhost:8000/student/questionBank.\n"
            from_address = 'placementcellvasavi@gmail.com'
            email_address = []
            with open("data.csv", 'r') as csvfile:
                reader = csv.reader(i.eligibleStudents) 
                for row in reader:
                    email_address.append(row[5])
                    send_mail(subject, content,from_address, email_address, fail_silently=False)
                    
                    

    mailCompany.short_description = "Mail the eligible students list to the company"
    mailStudents.short_description = "Mail all eligible students the question bank link"
    actions = ['mailCompany', 'mailStudents']
    

class QuestionBankFilterAdmin(AdminAdvancedFiltersMixin,admin.ModelAdmin):
    def downloadQuestions(self, request, queryset):
        f = StringIO()
        count = 1
        for i in queryset:
            f.write('Set '+str(count)+' '+str(i.date)+'\n\n')
            f.write(i.questions+'\n\n')

        f.seek(0)
        response = HttpResponse(f, content_type='text')
        response['Content-Disposition'] = 'attachment; filename = QuestionsList.txt'
        return response
        

    downloadQuestions.short_description = 'Download the questions'
    date_hierarchy = 'date'
    list_filter = ['date']
    advanced_filter_fields = [
        'company__companyName',
        'round_no',
    ]
    actions=['downloadQuestions']


class PlacedAdmin(AdminAdvancedFiltersMixin, admin.ModelAdmin):
    advanced_filter_fields = [
        'companyName',
        'payPackage',
        'year',
        'student__hallTicketNumber',
    ]
    def downloadCSV(self, request, queryset):
        f = StringIO()
        writer = csv.writer(f)
        writer.writerow(['Company','Package','Recruitment Year','Student Id'])
        for i in queryset:
            writer.writerow([i.companyName, i.payPackage, i.year, i.student.hallTicketNumber])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename = filtered-student-list.csv'
        return response

    downloadCSV.short_description = "Download list in csv format"
    actions = ['downloadCSV']
    


admin.site.register(StudentProfile,StudentProfileAdmin)
admin.site.register(Certificates)
admin.site.register(Placed, PlacedAdmin)
admin.site.register(Company, CompanyFilterAdmin)
admin.site.register(QuestionBank, QuestionBankFilterAdmin)
