from django.urls import path
from . import views

urlpatterns = [
     path('course/<int:course_id>/', views.course_detail, name='course_detail'),
     path('submit/<int:course_id>/', views.submit, name='submit'),
    path('result/<int:course_id>/<int:submission_id>/', views.show_exam_result, name='show_exam_result'),
    path('show_exam_result/', views.show_exam_result, name='show_exam_result'),
    path('final/', views.final_result, name='final_result'),
]