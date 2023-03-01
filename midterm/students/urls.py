from django.urls import path
from students import views

urlpatterns = [
    path('/api/students', views.students_handler),
    path('/api/students/<int:pk>', views.students_handler),
    

]

# /api/students    GET Student [] 
# /api/students    POST Student 
# /api/students/:id   GET Student 
# /api/students/:id   PUT Student 
# /api/students/:id   DELETE Student