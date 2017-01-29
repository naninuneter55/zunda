from django.contrib import admin

from quizzes.models import Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title',)
    inlines = [
        AnswerInline,
    ]

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')
    list_display_links = ('id', 'content',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)

admin.site.site_header = 'ずんだ管理画面'

