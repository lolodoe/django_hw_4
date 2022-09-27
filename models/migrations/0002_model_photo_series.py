# Generated by Django 4.1.1 on 2022-09-27 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='model',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos'),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='серия машины')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.model')),
            ],
        ),
    ]
