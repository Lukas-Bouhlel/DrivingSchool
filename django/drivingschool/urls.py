from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

from drivingschool import login, secretary, instructor, student, administrator

urlpatterns = [
    path('driving/', include('drivingapp.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('secretary/', secretary.home, name="secretary"),
    path('administrator/', administrator.home, name="administrator"),
    path('administrator/secretary/<int:id>', administrator.secretary, name="secretaryfromadministrator"),
    path('addsecretary/', administrator.addSecretary, name="addsecretary"),
    path('secretary/student/<int:id>', secretary.student, name="studentfromsecretary"),
    path('secretary/instructor/<int:id>', secretary.instructor, name="instructorfromsecretary"),
    path('secretary/planning/delete/<int:id>', secretary.deletePlanning, name="secretarydeleteplanning"),
    path('home', login.home),
    path('adduser/', secretary.addUser, name="adduser"),
    path('deleteuser/', secretary.deleteUser, name="deleteuser"),
    path('instructor/form/<int:id>', student.renderForm, name="studentform"),
    path('student/planning/', student.getPlanning, name="studentplanning"),
    path('instructor/planning/delete/<int:id>', instructor.delete, name="instructordeleteplanning"),
    path('instructor/', instructor.home, name="instructor"),
    path('instructor/student/<int:id>', instructor.student, name="studentfrominstructor"),
    path('instructor/delete/<int:id>', secretary.delete, name="instructordeletebysecretary")
]