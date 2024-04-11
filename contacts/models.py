from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=100, verbose_name="Телефон")
    message = models.TextField(verbose_name="Сообщение")
    is_helium = models.BooleanField( default=False, verbose_name="С гелием")
    is_painted = models.BooleanField( default=False, verbose_name="С рисунком")
    is_metallic = models.BooleanField( default=False, verbose_name="Металлический")
    is_foil = models.BooleanField( default=False, verbose_name="Фольгированный")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ["-created_at"]
