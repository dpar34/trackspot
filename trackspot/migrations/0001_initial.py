# Generated by Django 2.0.2 on 2018-03-23 13:34

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name for this album', max_length=100)),
                ('image_url', models.CharField(help_text='Enter a URL for the album art for this album', max_length=500, null=True)),
                ('release_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name for this artist', max_length=100)),
                ('bio', models.CharField(blank=True, help_text='Enter a description fot this artist', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name for this genre', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(help_text='Enter a description for this song', max_length=500)),
                ('rating', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trackspot.Album')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name for this song', max_length=100)),
                ('description', models.CharField(blank=True, help_text='Enter a description for this song', max_length=500)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackspot.Album')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='trackspot.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name for this user', max_length=50)),
                ('bio', models.CharField(help_text='Enter a bio for this user', max_length=500)),
                ('location', models.CharField(help_text='Enter a location for this user', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Critic',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='trackspot.User')),
                ('organization', models.CharField(help_text='Enter a location for this critic', max_length=50)),
            ],
            bases=('trackspot.user',),
        ),
        migrations.AddField(
            model_name='review',
            name='song',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trackspot.Song'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackspot.User'),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackspot.Artist'),
        ),
    ]
