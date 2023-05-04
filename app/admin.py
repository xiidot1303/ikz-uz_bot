from django.contrib import admin
from app.models import *
from app.forms import *

class LanguageAdmin(admin.ModelAdmin):
    list_display = ['user_ip', 'lang']

class QuestionAdmin(admin.ModelAdmin):
    list_display = []

admin.site.register(Language, LanguageAdmin)
admin.site.register(Question, QuestionAdmin)


admin.site.site_header = 'IKZ-uz admin'
admin.site.site_title = 'IKZ-uz'