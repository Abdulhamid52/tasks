# Generated by Django 3.2.5 on 2021-07-26 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0002_auto_20210726_1257'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=450, verbose_name='work name')),
                ('salary', models.IntegerField(default=0, verbose_name='salary')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_work', to=settings.AUTH_USER_MODEL)),
                ('workers', models.ManyToManyField(blank=True, to='accounts.Workers', verbose_name='workers')),
            ],
        ),
    ]
