from django.urls import path
from api.v1.general import views


urlpatterns=[
    path('register-student/',views.register_student),
    path('view-studentprofile/',views.view_studentprofile),
    path('edit-studentprofile/<pk>',views.edit_studentprofile),
    path('delete-studentprofile/<pk>',views.delete_studentprofile),

    path('create-chief-user/',views.create_chief_user),
    path('chief-login/',views.chief_login),
    path('student-login/',views.student_login),
   
    # path('login/',views.UserLogin),
  

]