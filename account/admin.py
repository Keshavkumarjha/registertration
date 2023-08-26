from django.contrib import admin

from account.models import CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):

    list_display = ('username','full_name', 'email', 'phone_number')
    search_fields = ['email','username']
  
admin.site.register(CustomUser, CustomUserAdmin)

