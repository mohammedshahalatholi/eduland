from django.urls import path
from . import views
urlpatterns = [
    path('courses/', views.courses,name='courses'),
    path('',views.samp),
    path('add/',views.adddata,name='add'),
    path('list/',views.list,name='list'),
    path('edit/<pk>',views.edit,name='edit'),
    path('delete/<pk>',views.delete,name='Delete')
]