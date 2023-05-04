from django.contrib import admin
from app.models import *
from app.forms import *
from django.urls import reverse
from django.utils.html import format_html

class LanguageAdmin(admin.ModelAdmin):
    list_display = ['user_ip', 'lang']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['index', 'text_ru', 'answer_similarity', 'datetime', 'edit_button']
    list_display_links = None
    list_filter = ['answer_similarity', 'datetime']
    sortable_by = ['index']
    search_fields = ['index', 'text_ru']
    
    def edit_button(self, obj):
        change_url = reverse('admin:app_question_change', args=[obj.id])
        return format_html('<a class="btn btn-primary" href="{}"><i class="fas fa-edit"></i></a>', change_url)
    edit_button.short_description = 'Действие'

admin.site.register(Language, LanguageAdmin)
admin.site.register(Question, QuestionAdmin)


admin.site.site_header = 'IKZ-uz admin'
admin.site.site_title = 'IKZ-uz'