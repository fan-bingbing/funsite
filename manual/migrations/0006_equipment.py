# Generated by Django 2.2.4 on 2019-08-22 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manual', '0005_delete_specan'),
    ]

    operations = [
        migrations.CreateModel(
            name='EQUIPMENT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_name', models.CharField(max_length=200)),
            ],
        ),
    ]
