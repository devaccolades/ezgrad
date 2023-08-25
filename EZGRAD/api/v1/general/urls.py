from django.urls import path
from api.v1.general import views


urlpatterns=[
    path('register-student/',views.register_student),
    path('view-studentprofile/',views.view_studentprofile),
    path('edit-studentprofile/<pk>',views.edit_studentprofile),
    path('delete-studentprofile/<pk>',views.delete_studentprofile),
    path('list-studentdetails/<pk>',views.list_studentdetails),
    path('list-studentprofile/<pk>',views.list_studentprofile),
    path('update-selected-option/<pk>',views.update_selected_option),
    path('save-student-review/',views.save_student_review),
    path('list-student-review/',views.list_student_review),
   

    path('create-chief-user/',views.create_chief_user),
    path('chief-login/',views.chief_login),
    path('student-login/',views.student_login),
   
    # path('login/',views.UserLogin),
  

]