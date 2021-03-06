# Generated by Django 2.2.7 on 2020-07-16 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.CharField(default='Y', max_length=30, verbose_name='active')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created_date')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='modified_date')),
                ('fname', models.CharField(max_length=30, verbose_name='stud_fname')),
                ('lname', models.CharField(max_length=30, verbose_name='stud_lname')),
                ('email', models.EmailField(max_length=254, verbose_name='stud_email')),
                ('dob', models.CharField(max_length=30, verbose_name='stud_dob')),
                ('contact', models.BigIntegerField(verbose_name='stud_mob')),
                ('qual', models.CharField(max_length=30, verbose_name='stud_qual')),
                ('gender', models.CharField(max_length=30, verbose_name='stud_gen')),
            ],
            options={
                'db_table': 'Stud_Info',
            },
        ),
    ]
