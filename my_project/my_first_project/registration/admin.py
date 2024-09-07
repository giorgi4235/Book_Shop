from django.contrib import admin

# Register your models here.


from .models import User,Profile
# Register your models here.



admin.site.register(User)
admin.site.register(Profile)