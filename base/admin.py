from django.contrib import admin
from .models import RoomMember,Message #added

# Register your models here.
admin.site.register(RoomMember)
admin.site.register(Message) #added