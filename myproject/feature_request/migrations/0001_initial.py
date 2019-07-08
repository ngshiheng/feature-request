# Generated by Django 2.2.3 on 2019-07-08 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('client', models.CharField(choices=[('A', 'Client A'), ('B', 'Client B'), ('C', 'Client C')], default='A', max_length=10)),
                ('priority', models.IntegerField()),
                ('target_date', models.DateField(auto_now=True)),
                ('product_area', models.CharField(choices=[('Assessments', 'Assessments'), ('Billing', 'Billing'), ('Recruit', 'Recruit'), ('Reports', 'Reports')], default='Assessments', max_length=20)),
            ],
        ),
    ]
