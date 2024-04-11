from typing import Iterable
from django.db import models


class BaloonColor(models.Model):
    name = models.CharField(
        max_length=255, 
        verbose_name="Название", 
        help_text="Название цвета"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата создания", 
        help_text="Дата и время создания записи"
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "Цвета"
        ordering = ["-created_at"]


class BaloonSize(models.Model):
    inch = models.PositiveIntegerField(
        verbose_name="Размер (дюймы)",
        help_text="Введите размер в дюймах."
    )
    sm = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        blank=True,
        null=True,
        verbose_name="Размер (сантиметры)",
        help_text="Введите размер в сантиметрах."
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата создания", 
        help_text="Дата и время создания записи"
    )

    def save(self, *args, **kwargs):
        if self.inch:
            self.sm = self.inch * 2.54  # 1 дюйм = 2.54 сантиметра
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.inch} дюймов / {self.sm} сантиметров"
    
    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'
        ordering = ["-created_at"]


class BaloonType(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Название",
        help_text="Введите название типа шарика."
    )
    type_price = models.PositiveIntegerField(
        default=150,
        verbose_name='Цена типа',
        help_text='Укажите цену для этого типа шарика.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата создания", 
        help_text="Дата и время создания записи"
    )

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Тип шарика"
        verbose_name_plural = "Типы шариков"
        ordering = ["-created_at"]



class PriceBaloonSpecifications(models.Model):
    helium = models.PositiveIntegerField(
        verbose_name="Цена гелия",
        help_text="Цена за шарик с гелием"
    )
    painted = models.PositiveIntegerField(
        verbose_name="Цена на рисунки",
        help_text="Цена за раскрашенный шарик"
    )
    metallic = models.PositiveIntegerField(
        verbose_name="Цена металлического",
        help_text="Цена за шарик с металлической поверхностью"
    )
    foil = models.PositiveIntegerField(
        verbose_name="Цена фольгированного",
        help_text="Цена за фольгированный шарик"
    )

    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата создания", 
        help_text="Дата и время создания записи"
    )

    def __str__(self) -> str:
        return f"h: {self.helium}, p: {self.painted}, m: {self.metallic}, f: {self.foil}"

    class Meta:
        verbose_name = "Цена характеристик"
        verbose_name_plural = "Цены характеристик"
        ordering = ["-created_at"]

        
class Baloon(models.Model):
    image = models.ImageField(
        upload_to="baloon-image",
        verbose_name="Изображение",
        help_text="Выберите изображение.",
        null=True
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок",
        help_text="Введите заголовок."
    )
    description = models.TextField(
        max_length=700,
        verbose_name="Описание",
        help_text="Введите описание."
    )
    baloon_color = models.ForeignKey(
        BaloonColor,
        on_delete=models.CASCADE,
        verbose_name="Цвет",
        help_text="Выберите цвет шарика."
    )
    baloon_size = models.ForeignKey(
        BaloonSize,
        on_delete=models.CASCADE,
        verbose_name="Размер",
        help_text="Выберите размер шарика."
    )
    baloon_type = models.ForeignKey(
        BaloonType,
        on_delete=models.CASCADE,
        verbose_name="Тип шарика",
        help_text="Выберите тип шарика."
    )
    is_helium = models.BooleanField(
        default=False,
        verbose_name="С гелием",
        help_text="Укажите, содержит ли этот тип шарика гелий."
    )
    is_painted = models.BooleanField(
        default=False,
        verbose_name="С рисунком",
        help_text="Укажите, имеет ли этот тип шарика рисунок."
    )
    is_metallic = models.BooleanField(
        default=False,
        verbose_name="Металлический",
        help_text="Укажите, является ли этот тип шарика металлическим."
    )
    is_foil = models.BooleanField(
        default=False,
        verbose_name="Фольгированный",
        help_text="Укажите, является ли этот тип шарика фольгированным."
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Цена",
        help_text="Укажите цену для этого типа шарика."
    )
    price_specifications = models.ForeignKey(
        PriceBaloonSpecifications,
        on_delete=models.CASCADE,
        verbose_name="Цена характеристик",
        help_text="Укажите цену для этого типа шарика.",
    )
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="Дата создания", 
        help_text="Дата и время создания записи"
    )

    def balloon_all_price(self, *args, **kwargs):
        check = self.price
        check += self.baloon_type.type_price
        
        if self.is_helium:
            check += self.price_specifications.helium
        
        if self.is_painted:
            check += self.price_specifications.painted 

        if self.is_metallic:
            check += self.price_specifications.metallic 
        
        if self.is_foil:
            check += self.price_specifications.foil
            
        return check
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Шарик"
        verbose_name_plural = "Шарики"
        ordering = ["-created_at"]


