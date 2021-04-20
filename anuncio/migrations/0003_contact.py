# Generated by Django 3.1.7 on 2021-04-18 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncio', '0002_delete_anuncioimagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('destinatario', models.EmailField(max_length=100)),
                ('messagem', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'contatos',
                'db_table': 'contato',
            },
        ),
    ]