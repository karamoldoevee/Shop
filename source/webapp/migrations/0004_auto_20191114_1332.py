# Generated by Django 2.1 on 2019-11-14 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20191111_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('new', 'Новый'), ('payed', 'Оплачен'), ('processing', 'Обработка'), ('delivered', 'Доставлен'), ('canceled', 'Отменён')], default='new', max_length=20, verbose_name='Статус'),
        ),
    ]