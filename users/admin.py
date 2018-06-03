from django.contrib import admin
from .models import User
from mygis.models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Mysite_Market)
admin.site.register(Mysite_Market_Message)
admin.site.register(Mysite_Food)
admin.site.register(Mysite_Asses)
admin.site.register(Mysite_DataTime)
admin.site.register(Mysite_PriceTask)
admin.site.register(Mysite_Target)
admin.site.register(Mysite_Community)
admin.site.register(Mysite_PeopleTask)
admin.site.register(Mysite_Store)
admin.site.register(Mysite_Restaurant)