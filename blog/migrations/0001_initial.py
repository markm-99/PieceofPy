# Generated by Django 2.0 on 2020-11-27 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogArticle',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mainApp.Page')),
                ('date', models.DateField(verbose_name='Post date')),
            ],
            bases=('mainApp.page',),
        ),
    ]
