from django.urls import path
from .views import home_api, Student

urlpatterns = [
    path("home-api/", home_api),
    path("<int:id>/", Student.as_view(), name="detail"),
    # path("<int:id>/", student_get_update_delete, name="detail"),
    # path("<int:id>/", StudentGetUpdateDelete.as_view(), name="detail"),
    # path("list-create-api/", student_list_create_api),
    # path("list-create-api/", StudentList.as_view()),
    # path("list-api/", student_list_api),
    # path("create-api/", student_create_api),
]
