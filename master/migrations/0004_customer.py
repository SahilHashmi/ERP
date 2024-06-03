# Generated by Django 5.0.6 on 2024-05-31 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_state_delete_statecode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_type', models.CharField(max_length=100)),
                ('preference_string', models.TextField()),
            ],
        ),
    ]