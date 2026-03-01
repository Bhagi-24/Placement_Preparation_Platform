from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('aptitude/', views.aptitude_test, name='aptitude_test'),
    path('technical/', views.technical_test, name='technical_test'),
    path('coding/', views.coding_test_intro, name='coding_intro'),
    path('coding/test/', views.coding_test, name='coding_test'),  # <--- important!
    path('coding/result/', views.coding_result, name='coding_result'),
    path('hr/', views.hr_company_select, name='hr_select'),
    path('hr/questions/<str:company>/', views.hr_questions, name='hr_questions'),
    path('resume_checker/', views.resume_checker, name='resume_checker')
]
