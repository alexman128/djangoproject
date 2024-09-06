from django.contrib import admin

# Register your models here.
from notification.models import BackendUser, Category, Channel

# Register your models here.
admin.site.register(BackendUser)
admin.site.register(Category)
admin.site.register(Channel)
