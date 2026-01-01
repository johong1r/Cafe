from django.db import models
from accounts.models import User
from django_resized import ResizedImageField


class Product(models.Model):
    image = ResizedImageField(size=[800, 600], crop=['middle', 'center'], upload_to='objects/', verbose_name='Изображение', 
                              null=True, blank=True, quality=90)
    name = models.CharField(max_length=100, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    description = models.CharField(max_length=1500, verbose_name='Описание')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Order {self.id} by {self.user.full_name}"
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrdemItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    quantity = models.PositiveIntegerField(verbose_name='Количество')

    def __str__(self):
        return self.order
    
    class Meta:
        verbose_name = 'Товар заказа'
        verbose_name_plural = 'Товары заказов'