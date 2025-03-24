
from django.urls import path
from rest_framework import routers

from note_app.views import RegisterView, LoginView, LogoutView, UserView
from note_app.viewsets import NoteViewSet

router = routers.DefaultRouter()
router.register('notes', NoteViewSet, basename='notes')
urlpatterns = router.urls
urlpatterns.append(path('register/', RegisterView.as_view(), name='register'))
urlpatterns.append(path('login/', LoginView.as_view(), name='login'))
urlpatterns.append(path('logout/', LogoutView.as_view(), name='logout'))
