# Generated by Django 4.0 on 2022-02-02 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '__first__'),
        ('todos', '0002_todos_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.customuser'),
        ),
    ]
