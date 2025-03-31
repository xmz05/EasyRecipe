from django.db import models

class Recipe(models.Model):
    CATEGORY_CHOICES = [
        ('breakfast', 'Завтрак'),
        ('lunch', 'Обед'),
        ('dinner', 'Ужин'),
        ('dessert', 'Десерт'),
        ('other', 'Другое'),
    ]

    
    title = models.CharField(max_length=200, verbose_name="Название")
    ingredients = models.TextField(verbose_name="Ингредиенты")
    instructions = models.TextField(verbose_name="Как приготовить")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name="Категория блюда")
    cooking_time = models.PositiveIntegerField(verbose_name="Время приготовления (мин)")
    calories = models.PositiveIntegerField(verbose_name="Калорийность (ккал)")

    def __str__(self):
        return self.title
