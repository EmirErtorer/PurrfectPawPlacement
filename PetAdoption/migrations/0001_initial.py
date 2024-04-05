# Generated by Django 5.0.4 on 2024-04-05 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('breed', models.CharField(max_length=100)),
                ('disability', models.CharField(blank=True, max_length=255)),
                ('pictures', models.ImageField(blank=True, null=True, upload_to='pets')),
                ('allergies', models.CharField(blank=True, max_length=255)),
                ('availability', models.BooleanField(default=True)),
                ('gender', models.CharField(max_length=50)),
                ('health_status', models.CharField(max_length=100)),
                ('videos', models.FileField(blank=True, null=True, upload_to='pet_videos')),
            ],
        ),
    ]