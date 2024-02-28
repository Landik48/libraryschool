from django.db import models

class catalog(models.Model):
    title = models.TextField("Название")
    description = models.TextField('Описание')
    availability = models.TextField("Наличие")
    author = models.TextField("Автор")
    genre = models.TextField("Жанр")
    img_link = models.TextField("Ссылка на изображение")

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Каталог книг'

class wishes(models.Model):
    title = models.CharField('Краткое описание', max_length = 50)
    description = models.TextField('Подробное описание преложения')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Книга пожеланий'