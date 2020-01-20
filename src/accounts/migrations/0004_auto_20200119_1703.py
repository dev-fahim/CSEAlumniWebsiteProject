# Generated by Django 3.0.2 on 2020-01-19 11:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20200119_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdetail',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sociallink',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='social', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
