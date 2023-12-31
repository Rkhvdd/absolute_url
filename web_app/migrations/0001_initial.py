# Generated by Django 4.2.2 on 2023-06-23 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('manufac_date', models.DateTimeField()),
                ('expir_date', models.DateTimeField()),
                ('mtype', models.CharField(choices=[('fst', 'Таблетки'), ('scn', 'Капсулы'), ('thrd', 'Мазь'), ('frth', 'Сироп')], max_length=30)),
                ('price', models.PositiveIntegerField()),
                ('decription', models.TextField()),
            ],
        ),
    ]
