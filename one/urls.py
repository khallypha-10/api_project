from django.urls import path
from . views import StudentList, stud, StudentRetrieve, StudentDelete, StudentCreate, StudentRetrieveUpdate
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('home', StudentList.as_view(), name="home"),
    path('create', StudentCreate.as_view(), name="create"),
    path('student/<pk>', StudentRetrieve.as_view(), name="retrieve"),
    path('student/<pk>/update', StudentRetrieveUpdate.as_view(), name="retrieve/update"),
    path('student/<pk>/delete', StudentDelete.as_view(), name="delete"),
    path('create', stud, name="create"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]