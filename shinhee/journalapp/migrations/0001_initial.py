# Generated by Django 4.2.2 on 2023-06-22 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JournalUseForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('pub_date', models.DateTimeField(verbose_name='data published')),
                ('weather', models.CharField(max_length=20)),
                ('journal', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='picture/')),
            ],
        ),
    ]