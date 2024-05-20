# Generated by Django 4.2.11 on 2024-04-03 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_cart_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('messeage_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('inquiry', models.CharField(max_length=300)),
            ],
        ),
    ]
