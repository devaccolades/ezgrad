from django.urls import path
from api.v1.question import views

urlpatterns=[
    path('add-question/',views.add_question),
    path('view-question/',views.view_question),
    path('edit-question/<int:id>',views.edit_question),
    path('delete-question/<int:id>',views.delete_question),

    path('add-options/',views.add_options),
    path('view-options/',views.view_options),
    path('edit-options/<pk>',views.edit_options),
    path('delete-options/<pk>',views.delete_options),

    path('add-answer/',views.add_answer),
    path('view-answer/',views.view_answer),
    path('delete-answer/<int:id>',views.delete_answer),

    

]