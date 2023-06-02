from django.contrib import admin
from .models import new_Authors
from .models import Codes

admin.site.register(Codes)
admin.site.register(new_Authors)

