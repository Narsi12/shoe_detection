# Generated by Django 4.1.13 on 2024-11-11 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShoeType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shoe_type', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('count', models.IntegerField()),
                ('product_path', models.CharField(max_length=255)),
                ('shoe_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shoe_app.shoetype')),
            ],
        ),
    ]
