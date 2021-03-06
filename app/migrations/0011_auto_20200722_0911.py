# Generated by Django 3.0.5 on 2020-07-22 03:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200721_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcatagory',
            name='cat_desc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='subcatagory',
            name='cat_icon',
            field=models.ImageField(default='cat_icons/AdminLTELogo.png', upload_to='cat_icons'),
        ),
        migrations.AlterField(
            model_name='subcatagory',
            name='cat_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='subcatagory',
            name='cat_title',
            field=models.CharField(choices=[('show', 'show'), ('hide', 'hide')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='subcatagory',
            name='clr_url',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='subcatagory',
            name='meta_desc',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='subcatagory',
            name='meta_key',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='subcatagory',
            name='par_cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Catagory'),
        ),
    ]
