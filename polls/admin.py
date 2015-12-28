from django.contrib import admin

# Register your models here.
from .models import *

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class VoteAdmin(admin.ModelAdmin):
    list_display = ('question','choice', 'user', 'vote_time')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Vote, VoteAdmin)