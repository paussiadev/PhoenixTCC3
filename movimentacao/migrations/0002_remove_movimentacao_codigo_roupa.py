# Generated by Django 5.1.1 on 2024-10-04 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movimentacao', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimentacao',
            name='codigo_roupa',
        ),
    ]
