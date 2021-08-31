from django.contrib import admin
from .models import Question
from .views import ContactFormView
admin.site.register()
admin.site.register(Question)
admin.site.register(ContactFormView)

# Register your models here.
