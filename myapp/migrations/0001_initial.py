# Generated by Django 4.2.7 on 2024-02-08 06:14

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('BranchCode', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('Company', models.CharField(max_length=50)),
                ('Location', models.CharField(max_length=50)),
                ('Employees', models.CharField(max_length=10)),
                ('BranchImage', models.ImageField(blank=True, null=True, upload_to='branch_image/')),
            ],
        ),
        migrations.CreateModel(
            name='DailyRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empname', models.CharField(default='Unknown', max_length=50)),
                ('date', models.DateField(default=datetime.date.today)),
                ('timein', models.TimeField(blank=True, null=True)),
                ('timeout', models.TimeField(blank=True, null=True)),
                ('breakout', models.TimeField(blank=True, null=True)),
                ('breakin', models.TimeField(blank=True, null=True)),
                ('totallateness', models.CharField(default='00:00', max_length=50)),
                ('latecount', models.CharField(default='0', max_length=6)),
                ('totalundertime', models.CharField(default='00:00', max_length=8)),
                ('totalovertime', models.CharField(default='00:00', max_length=8)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('approveOT', models.BooleanField(default=False)),
                ('branch_name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'attendance',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmpCode', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('Firstname', models.CharField(max_length=20)),
                ('Middlename', models.CharField(max_length=20)),
                ('Lastname', models.CharField(max_length=20)),
                ('DateofBirth', models.DateField(default=datetime.date(2000, 1, 1))),
                ('BloodType', models.CharField(default='N/D', max_length=3)),
                ('Gender', models.CharField(default='Male', max_length=8)),
                ('CivilStatus', models.CharField(default='N/A', max_length=10)),
                ('Address', models.CharField(default='N/D', max_length=50)),
                ('Position', models.CharField(max_length=50)),
                ('Department', models.CharField(blank=True, default='N/A', max_length=50, null=True)),
                ('EmployementDate', models.DateField(default=datetime.date(2000, 1, 1))),
                ('EmploymentStatus', models.CharField(default='Regular', max_length=15)),
                ('EmpImage', models.ImageField(blank=True, null=True, upload_to='emp_image/')),
                ('BranchCode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.branches')),
            ],
        ),
        migrations.CreateModel(
            name='temporay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_number', models.CharField(max_length=100)),
                ('Empname', models.CharField(default='Unknown', max_length=50)),
                ('date', models.DateField(default=datetime.date.today)),
                ('timein_names', models.CharField(blank=True, max_length=100, null=True)),
                ('timeout_names', models.CharField(blank=True, max_length=100, null=True)),
                ('breakout_names', models.CharField(blank=True, max_length=100, null=True)),
                ('breakin_names', models.CharField(blank=True, max_length=100, null=True)),
                ('timein_timestamps', models.DateTimeField(blank=True, null=True)),
                ('breakout_timestamps', models.DateTimeField(blank=True, null=True)),
                ('breakin_timestamps', models.DateTimeField(blank=True, null=True)),
                ('timeout_timestamps', models.DateTimeField(blank=True, null=True)),
                ('afternoonBreakin_timestamps', models.DateTimeField(blank=True, null=True)),
                ('afternoonTimeout_timestramps', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'temporay',
            },
        ),
        migrations.CreateModel(
            name='RequestForm',
            fields=[
                ('FormID', models.AutoField(primary_key=True, serialize=False)),
                ('SelectRequest', models.CharField(max_length=30)),
                ('BeginTimeOff', models.DateTimeField()),
                ('ConcludeTimeOff', models.DateTimeField()),
                ('Range', models.CharField(default='N/A', max_length=10)),
                ('isApproved', models.BooleanField(default=False)),
                ('Remarks', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('date', models.DateField(default=datetime.date(2000, 1, 1))),
                ('EmpCode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RequestDate', models.DateField(default=datetime.date(2000, 1, 1))),
                ('RequestForm', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.requestform')),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vacation', models.FloatField(default=0)),
                ('Sick', models.FloatField(default=0)),
                ('GracePeriod', models.IntegerField(default=15)),
                ('last_grace_period_month', models.DateTimeField(default=datetime.date(2024, 1, 1))),
                ('last_leaves_year', models.DateField(default=datetime.date(2024, 1, 1))),
                ('EmpCode', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.employee')),
            ],
        ),
    ]
