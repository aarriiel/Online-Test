import uuid

from django.db import models


class Category(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    label = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.label

    def save(self, *args, **kwargs):
        self.id = uuid.uuid1()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = '種類'
        verbose_name_plural = '種類'


class Size(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    label = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.label

    def save(self, *args, **kwargs):
        self.id = uuid.uuid1()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = '尺寸'
        verbose_name_plural = '尺寸'


class Color(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    label = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.label

    def save(self, *args, **kwargs):
        self.id = uuid.uuid1()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = '顏色'
        verbose_name_plural = '顏色'


class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        verbose_name='種類'
    )
    size = models.ManyToManyField(
        Size
    )
    unit_prize = models.PositiveIntegerField(default=0)
    inventory = models.PositiveIntegerField(default=0)
    color = models.ManyToManyField(
        Color
    )

    def save(self, *args, **kwargs):
        self.id = uuid.uuid1()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = '產品'
        verbose_name_plural = '產品'


