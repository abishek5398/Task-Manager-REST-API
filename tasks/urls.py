from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet,UserRegistrationView
router = DefaultRouter()
router.register('tasks',TaskViewSet)

urlpatterns = [
     path('register/',UserRegistrationView.as_view()),
    *router.urls
]