from django.db import models


class AuthorModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'
        ordering = ['-id']


class BookModel(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE)
    publication_date = models.DateField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
        ordering = ['-id']
