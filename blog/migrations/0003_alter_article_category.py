# Generated by Django 4.0.5 on 2022-06-14 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_article_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='blog.category', verbose_name='카테고리'),
        ),
    ]