from django.db import models

from work_space.models import WorkSpace


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.CharField(max_length=255,
                                   null=True,
                                   blank=True,
                                   verbose_name='Описание')
    brand = models.ForeignKey('Brand',
                              on_delete=models.CASCADE,
                              related_name='products',
                              verbose_name='Бренд')
    category = models.ForeignKey('Category',
                                 on_delete=models.CASCADE,
                                 related_name='products',
                                 verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена')
    quantity = models.IntegerField(verbose_name='Количество')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата создания')
    plase_of_origin = models.ForeignKey(WorkSpace,
                                        on_delete=models.CASCADE,
                                        verbose_name='Место хранения')

    def __str__(self):
        return f'{self.title} - {self.category} - {self.brand}'


class Category(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name='Название',
                             unique=True)
    description = models.CharField(max_length=255,
                                   null=True,
                                   blank=True,
                                   verbose_name='Описание')

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=255,
                             verbose_name='Название',
                             unique=True)
    description = models.CharField(max_length=255,
                                   null=True,
                                   blank=True,
                                   verbose_name='Описание')

    def __str__(self):
        return self.title
