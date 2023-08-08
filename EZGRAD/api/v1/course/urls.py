from django.urls import path
from api.v1.course import views

urlpatterns=[

    path('add-university/',views.add_university),
    path('view-university/',views.view_university),
    path('edit-university/<pk>',views.edit_university),
    path('delete-university/<pk>',views.delete_university),
    path('university-list/',views.university_list),
    path('fact-list/',views.fact_list),
    path('approval-list/',views.approval_list),
    path('list-university-logo/',views.list_university_logo),
    path('list-universitylogo-studentform/',views.list_universitylogo_studentform),
    path('list-popular-university',views.list_popular_university),

    path('add-facts/',views.add_facts),
    path('view-facts/',views.view_facts),
    path('edit-facts/<int:id>',views.edit_facts),
    path('delete-facts/<int:id>',views.delete_facts),

    path('add-approval/',views.add_approval),
    path('view-approval/',views.view_approval),
    path('edit-approval/<int:id>',views.edit_approval),
    path('delete-approval/<int:id>',views.delete_approval),

    path('add-course/',views.add_course),
    path('view-course/',views.view_course),
    path('edit-course/<pk>',views.edit_course),
    path('delete-course/<pk>',views.delete_course),
    path('list-courses/',views.list_courses),
    path('list-course-studentform/',views.list_course_studentform),

    path('add-specialization/',views.add_specialization),
    path('view-specialization/',views.view_specialization),
    path('edit-specialization/<int:id>',views.edit_specialization),
    path('delete-specialization/<int:id>',views.delete_specialization),
    path('list-specialization/<pk>',views.list_specialization),

    path('add-country/',views.add_country),
    path('view-country/',views.view_country),
    path('edit-country/<int:id>',views.edit_country),
    path('delete-country/<int:id>',views.delete_country),

    path('add-faq/',views.add_faq),
    path('view-faq/',views.view_faq),
    path('edit-faq/<int:id>',views.edit_faq),
    path('delete-faq/<int:id>',views.delete_faq),
    path('list-faq/<pk>',views.list_faq),

 

   

   
    
 




  

    

]