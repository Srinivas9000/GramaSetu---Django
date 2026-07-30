from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('services/', views.services, name='services'),
<<<<<<< HEAD
    path("issue/", views.issue, name="issue"),
    path('community/', views.community, name='community'),
    path('delete-issue/<int:issue_id>/', views.delete_issue, name='delete_issue'),
    path('elections/', views.elections, name='elections'),
    path('ward-1/', views.ward_1, name='ward-1'),
    path('ward-2/', views.ward_2, name='ward-2'),
    path('ward-3/', views.ward_3, name='ward-3'),
    path('ward-4/', views.ward_4, name='ward-4'),
    path('ward-5/', views.ward_5, name='ward-5'),       
    path('ward-6/', views.ward_6, name='ward-6'),
    path('ward-7/', views.ward_7, name='ward-7'),
    path('ward-8/', views.ward_8, name='ward-8'),
    path('ward-9/', views.ward_9, name='ward-9'),
    path('ward-10/', views.ward_10, name='ward-10'),
    path('govtactivities/', views.govtactivities, name='govtactivities'),
    path('employeeinformation/', views.employeeinformation, name='employeeinformation'),
    path('localactivities/', views.localactivities, name='localactivities'),
=======
>>>>>>> 94fe287e9a4711d1c632e1ba87a93186096f6d30
]
