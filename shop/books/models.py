from django.db import models

class Publisher(models.Model):
    name = models.CharField('Издательство', max_length=30)
    address = models.CharField('Адрес', blank=True, max_length=60)
    city = models.CharField('Город', blank=True, max_length=30)
    region = models.CharField('Область', blank=True, max_length=30)
    country = models.CharField('Страна', max_length=30)
    website = models.URLField('Сайт', blank=True,)
    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    email = models.EmailField(blank=True)
    def __str__(self):
        return '%s %s' % (self.last_name, self.first_name)

class Book(models.Model):
    title = models.CharField('Название', max_length=50)
    authors = models.ManyToManyField(Author, verbose_name='Авторы')
    publisher = models.ForeignKey(Publisher, verbose_name='Издательство')
    publication_date =  models.DateField('Дата публикации', blank=True, null=True)
    def __str__(self):
        return self.title