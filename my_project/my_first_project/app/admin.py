from django.contrib import admin
from .models import Student,StudentProfile,Book,Review,Order
# Register your models here.


admin.site.register(Student)
admin.site.register(StudentProfile)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Order)