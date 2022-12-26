# Generated by Django 4.1.4 on 2022-12-26 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('family', '0002_familiares_surname_alter_familiares_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='people',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('hijos', models.BooleanField()),
            ],
        ),
    ]