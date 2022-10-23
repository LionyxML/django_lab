from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(maxlength=100)
    body = models.TextField()
    author = models.ForeignKey(
        Author, relatedname="posts", on_delete=models.CASCADE
    )

    def str(self):
        return self.title
