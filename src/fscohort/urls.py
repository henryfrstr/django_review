from django.urls import path
from .views import home_view, student_list

urlpatterns = [
    path("", home_view),
    path("list/", student_list),
    # path("about/", about)
]
