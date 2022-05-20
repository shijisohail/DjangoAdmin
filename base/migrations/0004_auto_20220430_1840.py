# Generated by Django 3.2.9 on 2022-04-30 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0003_alter_room_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('hosts', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('topics', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.topics')),
            ],
        ),
        migrations.RenameModel(
            old_name='Messages',
            new_name='Message',
        ),
        migrations.DeleteModel(
            name='Death',
        ),
    ]
