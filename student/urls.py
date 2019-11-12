from django.urls import path
from . import views

urlpatterns = [
    path('placementform', views.placementform,name='placementform'),
    path('create', views.createStudent, name="create"),
    path('questionBank',views.questionBank,name='questionBank'),
    path('storeQuestionBank',views.storeQuestionBank,name='storeQuestionBank'),
    path('form',views.form,name='form'),
    path('bank',views.bank,name ='bank'),
    path('submit_successful',views.submit_successful,name='submit_successful')
]