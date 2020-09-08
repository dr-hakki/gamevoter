from django.contrib import admin

from .models import Question, Choice, Application, New

admin.site.site_header = "GameVoter Admin"
admin.site.site_title = "GameVoter Admin Area"
admin.site.index_title = "Welcome to the GameVoter admin area"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ["popular",'question_text',"choice_number","image","category","xcategory","creator"]}),
                  ]
    inlines = [ChoiceInline]



# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Application)
admin.site.register(New)