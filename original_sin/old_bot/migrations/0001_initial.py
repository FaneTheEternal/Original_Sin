# Generated by Django 3.0.5 on 2020-09-06 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VkUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(verbose_name='id пользователя')),
                ('status', models.IntegerField(default=0, verbose_name='текущей статус общения с ботом')),
            ],
        ),
        migrations.CreateModel(
            name='QuestProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.TextField(blank=True, null=True, verbose_name='Json с прогрессом')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quest_profile', to='old_bot.VkUser', verbose_name='Профиль')),
            ],
        ),
        migrations.CreateModel(
            name='IncomingProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=0, verbose_name='Статус общения')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incoming_profile', to='old_bot.VkUser', verbose_name='Профиль')),
            ],
        ),
        migrations.CreateModel(
            name='GameProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('some_data', models.TextField(default='{}', verbose_name='JSON фигня')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='old_bot.VkUser', verbose_name='Пользователь')),
            ],
        ),
    ]