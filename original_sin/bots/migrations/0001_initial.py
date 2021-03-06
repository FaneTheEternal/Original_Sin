# Generated by Django 3.1.7 on 2021-04-30 09:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, verbose_name='Code')),
                ('on', models.ManyToManyField(related_name='_botstep_on_+', to='bots.BotStep')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, verbose_name='Code')),
                ('location', models.UUIDField(verbose_name='Код текущего шага')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BotStepProxy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Текст')),
                ('on', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='bots.botstep')),
                ('to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_options', to='bots.botstep')),
            ],
        ),
    ]
