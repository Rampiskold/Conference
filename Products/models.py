from django.db import models
from django.utils.text import slugify

        
class Genre(models.Model):  #создаём класс(таблицу данных)
    genre = models.CharField('название жанра', max_length=256) # Создаём поле char с максимальной длинной 256 символов
    created = models.DateTimeField(auto_now_add=True)  # Дата сощздания записи
    updated = models.DateTimeField(auto_now=True)  # Дата изменения записи
    slug = models.SlugField(                         # это короткое название-метка, улучшает поиск в браузере.
        'slug',
        allow_unicode=True, max_length=254, blank=True)

    def __str__(self):
        return self.genre

    class Meta: 
        verbose_name='Жанр'  # отображение на сайте в админке
        verbose_name_plural='Жанры'  

    def save(self, *args, **kwargs):
        self.autoslug() # Делаем slug
        super(Genre, self).save(*args, **kwargs) # сохраняем

    def autoslug(self):
        if self.name:
            self.slug = slugify(self.name, allow_unicode=True)


class Customers(models.Model):
    email = models.EmailField('email', blank=True, null=True, default=None)  
    name = models.CharField('Имя', max_length=256)  
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name='Покупатель'
        verbose_name_plural='Покупатели'

    def save(self, *args, **kwargs):
        super(Customers, self).save(*args, **kwargs)


class Developers(models.Model):
    name = models.CharField('Название', max_length=512)  
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  
    slug = models.SlugField(
        'slug',
        allow_unicode=True, max_length=254, blank=True)  

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name='Разработчик'
        verbose_name_plural='Разработчики'

    def save(self, *args, **kwargs):
        self.autoslug()
        super(Developers, self).save(*args, **kwargs)


class Images(models.Model):
    images = models.ImageField(
        'фото',
        upload_to='game_image/',
        blank=True, null=True, default=None)  
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  

    class Meta: 
        verbose_name='Кртинка'  
        verbose_name_plural='Картинки'  

    def save(self, *args, **kwargs):
        super(Images, self).save(*args, **kwargs)

    def autoslug(self):
        if self.name:
            self.slug = slugify(self.name, allow_unicode=True)


class Games(models.Model):
    name = models.CharField('Название игры', max_length=512) 
    dev = models.ForeignKey(Developers, verbose_name='Разработчик',default=None)  
    discripshion = models.TextField('Описание', blank=True, null=True, default=None)  
    gener = models.ForeignKey(Genre, verbose_name='Жанр', blank=True, null=True, default=None)  
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  
    slug = models.SlugField(
        'slug',
        allow_unicode=True, max_length=254, blank=True)  
    images = models.ForeignKey(Images, verbose_name='Картинка', 
        blank=True, null=True, default=None)  
    price = models.DecimalField('Цена',max_digits=10, decimal_places=2, default=0)  

    #def __str__(self):
    #    return 

    class Meta: 
        verbose_name='Игра'  
        verbose_name_plural='Игры'  

    def save(self, *args, **kwargs):
        self.autoslug()
        super(Games, self).save(*args, **kwargs)

    def autoslug(self):
        if self.name:
            self.slug = slugify(self.name, allow_unicode=True)