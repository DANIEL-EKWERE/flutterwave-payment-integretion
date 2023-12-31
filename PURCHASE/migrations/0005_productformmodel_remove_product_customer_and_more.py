# Generated by Django 4.0.6 on 2023-06-29 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PURCHASE', '0004_customer_product_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
