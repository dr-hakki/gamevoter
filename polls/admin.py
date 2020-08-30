from django.contrib import admin

from .models import Question, Choice

admin.site.site_header = "GameVoter Admin"
admin.site.site_title = "GameVoter Admin Area"
admin.site.index_title = "Welcome to the GameVoter admin area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text',"choice_number","category","vdq"]}),
                 ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
                  ]
    inlines = [ChoiceInline]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)