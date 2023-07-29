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
    path('list-countries/',views.list_countries),




  

    

]