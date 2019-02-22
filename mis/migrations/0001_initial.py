# Generated by Django 2.1.5 on 2019-02-06 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country_Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('District_Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Klass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Klass', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=200)),
                ('Last_Name', models.CharField(max_length=200)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('Guadian_Contact', models.CharField(max_length=200)),
                ('Citizenship', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mis.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='Class_Teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mis.Teacher'),
        ),
        migrations.AddField(
            model_name='student',
            name='District',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mis.District'),
        ),
        migrations.AddField(
            model_name='student',
            name='Klass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mis.Klass'),
        ),
    ]