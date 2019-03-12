# api/urls.py
from django.urls import path

from . import views
# urlpatterns = [
#     # path('list', views.ListTodo.as_view()),
#     # path('update/<int:pk>', views.UpdateTodo.as_view()),
#     # path('<int:pk>/', views.DetailTodo.as_view()),
#     # path('DestroyTodo/<int:pk>/', views.DestroyTodo.as_view()),
#
#
# ]

# ModelViewSet which automatically provides list as well as
# create, retrieve, update, and destroy actions for us.

from .views import TodoViewSet

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('', TodoViewSet, base_name='todos')

urlpatterns =[
    path('', views.api_root),
    path('users/', views.UserList.as_view() , name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(),name='user'),
    path('snippets/', views.SnippetList.as_view(),name='snippest-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(),name='snippest'),
]
urlpatterns += router.urls

