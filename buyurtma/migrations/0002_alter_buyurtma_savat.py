# Generated by Django 4.0.3 on 2022-03-28 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyurtma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyurtma',
            name='savat',
            field=models.ManyToManyField(related_name='b_savatlari', to='buyurtma.savat'),
        ),
    ]
