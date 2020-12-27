from django.urls import path
<<<<<<< HEAD
from .views import home_view, student_list, student_add, student_detail, student_delete, student_update
=======
from .views import home_view, student_list, student_add, student_detail, student_delete,student_update
>>>>>>> 4759febfb8c689770388e7eed9e17cbb109e7f02

urlpatterns = [
    path("", home_view, name="home"),
    path("list/", student_list, name="list"),
    path("add/", student_add, name="add"),
    path("<int:id>", student_detail, name="detail"),
    path("<int:id>/delete", student_delete, name="delete"),
<<<<<<< HEAD
    path("<int:id>/update", student_update, name="update"),
=======
    path("<int:id>/update", student_update,name='update'),
>>>>>>> 4759febfb8c689770388e7eed9e17cbb109e7f02
    # path("about/", about)
]
# localhost/1/delete
