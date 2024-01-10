from django.contrib import admin
from management.models import signupdata
from management.models import contact

# Register your models here.
class servicesignupdata(admin.ModelAdmin):
    list_display = ['firstname','lastname','email','username','password1']
    
class servicecontact(admin.ModelAdmin):
    list_display = ['firstname','lastname','email','concern']
    

admin.site.register(signupdata,servicesignupdata)
admin.site.register(contact,servicecontact)