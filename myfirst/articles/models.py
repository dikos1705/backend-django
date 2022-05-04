from django.db import models
import datetime
from django.utils import timezone


class Article(models.Model):
    title = models.CharField('Название статьи',max_length=255)
    text = models.TextField('Текст статьи')
    pub_date = models.DateTimeField('дата публикации')
    def __str__(self):
        return f'{self.title} {self.text} {self.pub_date}'
    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
    def was_published_recently(self):
        return self.pub_date >=(timezone.now() - datetime.timedelta(days=7)) 
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    author_name=models.CharField('имя автора',max_length=50)
    comment_text = models.CharField('текст комментария', max_length=250)
    def __str__(self):
        return f'{self.article} {self.author_name} {self.comment_text}'
    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Комментарии"