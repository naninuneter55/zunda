from django.db import models

class Question(models.Model):
    title = models.CharField('タイトル', max_length=256)
    question = models.TextField('問題文', max_length=1024)
    correct_answer = models.CharField('正解', max_length=256)

    def __str__(self):
        return "{}".format(self.title)

    class Meta:
        verbose_name = '問題'
        verbose_name_plural = '問題'

class Answer(models.Model):
    question = models.ForeignKey(Question, verbose_name = '問題')
    content = models.CharField('回答内容', max_length=256)

    class Meta:
        verbose_name = '回答'
        verbose_name_plural = '回答'

