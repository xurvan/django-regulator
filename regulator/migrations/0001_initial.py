# Generated by Django 3.2.5 on 2021-08-09 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(db_index=True, null=True)),
                ('inserted_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True)),
                ('rate', models.TextField()),
                ('regex', models.TextField(unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
