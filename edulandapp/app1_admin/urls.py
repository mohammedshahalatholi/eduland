from django.urls import path
from . import views
urlpatterns = [
    path('load/', views.print),
    path('',views.load),
    path('add/',views.adddata,name='add'),
    path('list/',views.list,name='list'),
    path('edit/<pk>',views.edit,name='edit'),
    path('delete/<pk>',views.delete,name='Delete')
]