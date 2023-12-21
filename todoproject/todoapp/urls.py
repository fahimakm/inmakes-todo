from django.urls import path
from . import views

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('cbvhome/',views.tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.taskdetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.taskupdateview.as_view(),name='cbvupdate')
]
