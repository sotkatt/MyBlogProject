# Generated by Django 5.0.3 on 2024-03-26 11:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaloonColor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Название цвета', max_length=255, verbose_name='Название')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата и время создания записи', verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Цвет',
                'verbose_name_plural': 'Цвета',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='BaloonSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inch', models.PositiveIntegerField(help_text='Введите размер в дюймах.', verbose_name='Размер (дюймы)')),
                ('sm', models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Введите размер в сантиметрах.', max_digits=10, null=True, verbose_name='Размер (сантиметры)')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата и время создания записи', verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Размер',
                'verbose_name_plural': 'Размеры',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='BaloonType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название типа шарика.', max_length=255, verbose_name='Название')),
                ('type_price', models.PositiveIntegerField(default=150, help_text='Укажите цену для этого типа шарика.', verbose_name='Цена типа')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата и время создания записи', verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Тип шарика',
                'verbose_name_plural': 'Типы шариков',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='PriceBaloonSpecifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('helium', models.PositiveIntegerField(help_text='Цена за шарик с гелием', verbose_name='Цена гелия')),
                ('painted', models.PositiveIntegerField(help_text='Цена за раскрашенный шарик', verbose_name='Цена на рисунки')),
                ('metallic', models.PositiveIntegerField(help_text='Цена за шарик с металлической поверхностью', verbose_name='Цена металлического')),
                ('foil', models.PositiveIntegerField(help_text='Цена за фольгированный шарик', verbose_name='Цена фольгированного')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата и время создания записи', verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Цена характеристик',
                'verbose_name_plural': 'Цены характеристик',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Baloon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(help_text='Выберите изображение.', null=True, upload_to='baloon-image', verbose_name='Изображение')),
                ('title', models.CharField(help_text='Введите заголовок.', max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(help_text='Введите описание.', max_length=700, verbose_name='Описание')),
                ('is_helium', models.BooleanField(default=False, help_text='Укажите, содержит ли этот тип шарика гелий.', verbose_name='С гелием')),
                ('is_painted', models.BooleanField(default=False, help_text='Укажите, имеет ли этот тип шарика рисунок.', verbose_name='С рисунком')),
                ('is_metallic', models.BooleanField(default=False, help_text='Укажите, является ли этот тип шарика металлическим.', verbose_name='Металлический')),
                ('is_foil', models.BooleanField(default=False, help_text='Укажите, является ли этот тип шарика фольгированным.', verbose_name='Фольгированный')),
                ('price', models.DecimalField(decimal_places=2, default=0, help_text='Укажите цену для этого типа шарика.', max_digits=10, verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата и время создания записи', verbose_name='Дата создания')),
                ('baloon_color', models.ForeignKey(help_text='Выберите цвет шарика.', on_delete=django.db.models.deletion.CASCADE, to='blog.balooncolor', verbose_name='Цвет')),
                ('baloon_size', models.ForeignKey(help_text='Выберите размер шарика.', on_delete=django.db.models.deletion.CASCADE, to='blog.baloonsize', verbose_name='Размер')),
                ('baloon_type', models.ForeignKey(help_text='Выберите тип шарика.', on_delete=django.db.models.deletion.CASCADE, to='blog.baloontype', verbose_name='Тип шарика')),
                ('price_specifications', models.ForeignKey(help_text='Укажите цену для этого типа шарика.', on_delete=django.db.models.deletion.PROTECT, to='blog.pricebaloonspecifications', verbose_name='Цена характеристик')),
            ],
            options={
                'verbose_name': 'Шарик',
                'verbose_name_plural': 'Шарики',
                'ordering': ['-created_at'],
            },
        ),
    ]
