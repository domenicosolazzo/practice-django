from django.contrib import admin
from polls.models import Question, Choice

#admin.site.register(Question)

class QuestionAdmin(admin.Models):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)
