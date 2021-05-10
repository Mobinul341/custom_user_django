from django.db import models

class ArticleModel(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
