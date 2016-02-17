# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-17 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_auto_20160216_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antropometricmeasurement',
            name='chest',
            field=models.FloatField(blank=True, null=True, verbose_name='Perim. Chest'),
        ),
        migrations.AlterField(
            model_name='antropometricmeasurement',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Date of measurement'),
        ),
        migrations.AlterField(
            model_name='antropometricmeasurement',
            name='hip',
            field=models.FloatField(blank=True, null=True, verbose_name='Perim. Hips'),
        ),
        migrations.AlterField(
            model_name='antropometricmeasurement',
            name='imc',
            field=models.FloatField(blank=True, null=True, verbose_name='I.M.C.'),
        ),
        migrations.AlterField(
            model_name='antropometricmeasurement',
            name='lost_cm',
            field=models.FloatField(blank=True, null=True, verbose_name='Lost cm (waist)'),
        ),
        migrations.AlterField(
            model_name='antropometricmeasurement',
            name='lost_cm_total',
            field=models.FloatField(blank=True, null=True, verbose_name='Lost cm total (waist)'),
        ),
        migrations.AlterField(
            model_name='antropometricmeasurement',
            name='lost_weight',
            field=models.FloatField(blank=True, null=True, verbose_name='Lost weight'),
        ),
        migrations.AlterField(
            model_name='antropometricmeasurement',
            name='lost_weight_total',
            field=models.FloatField(blank=True, null=True, verbose_name='Lost weight total'),
        ),
        migrations.AlterField(
            model_name='antropometricmeasurement',
            name='min_waist',
            field=models.FloatField(blank=True, null=True, verbose_name='Perim. Waist Min'),
        ),
        migrations.AlterField(
            model_name='antropometricmeasurement',
            name='navel',
            field=models.FloatField(blank=True, null=True, verbose_name='Perim. Navel'),
        ),
        migrations.AlterField(
            model_name='antropometricmeasurement',
            name='thigh',
            field=models.FloatField(blank=True, null=True, verbose_name='Perim. Thighs'),
        ),
        migrations.AlterField(
            model_name='antropometricmeasurement',
            name='weight',
            field=models.FloatField(blank=True, null=True, verbose_name='Weight'),
        ),
        migrations.AlterField(
            model_name='biochemanalysis',
            name='calcium',
            field=models.FloatField(blank=True, null=True, verbose_name='Calcium'),
        ),
        migrations.AlterField(
            model_name='biochemanalysis',
            name='cholesterol_total',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Cholesterol Total'),
        ),
        migrations.AlterField(
            model_name='biochemanalysis',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Date of analysis'),
        ),
        migrations.AlterField(
            model_name='biochemanalysis',
            name='hdl',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Cholesterol HDL'),
        ),
        migrations.AlterField(
            model_name='biochemanalysis',
            name='iron',
            field=models.FloatField(blank=True, null=True, verbose_name='Iron'),
        ),
        migrations.AlterField(
            model_name='biochemanalysis',
            name='ldl',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Cholesterol LDL'),
        ),
        migrations.AlterField(
            model_name='biochemanalysis',
            name='sugar_level',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Sugar Level'),
        ),
        migrations.AlterField(
            model_name='biochemanalysis',
            name='tg_level',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Triglycerids Level'),
        ),
        migrations.AlterField(
            model_name='biochemanalysis',
            name='uric_acid',
            field=models.FloatField(blank=True, null=True, verbose_name='Uric Acid'),
        ),
        migrations.AlterField(
            model_name='bloodpressure',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Date of report'),
        ),
        migrations.AlterField(
            model_name='bloodpressure',
            name='heart_rate',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Heart Rate'),
        ),
        migrations.AlterField(
            model_name='bloodpressure',
            name='left_arm_high',
            field=models.FloatField(blank=True, null=True, verbose_name='Left Arm High'),
        ),
        migrations.AlterField(
            model_name='bloodpressure',
            name='left_arm_low',
            field=models.FloatField(blank=True, null=True, verbose_name='Left Arm Low'),
        ),
        migrations.AlterField(
            model_name='bloodpressure',
            name='mean_high',
            field=models.FloatField(blank=True, null=True, verbose_name='Mean High'),
        ),
        migrations.AlterField(
            model_name='bloodpressure',
            name='mean_low',
            field=models.FloatField(blank=True, null=True, verbose_name='Mean Low'),
        ),
        migrations.AlterField(
            model_name='bloodpressure',
            name='right_arm_high',
            field=models.FloatField(blank=True, null=True, verbose_name='Right Arm High'),
        ),
        migrations.AlterField(
            model_name='bloodpressure',
            name='right_arm_low',
            field=models.FloatField(blank=True, null=True, verbose_name='Right Arm Low'),
        ),
        migrations.AlterField(
            model_name='bloodpressure',
            name='treatment',
            field=models.NullBooleanField(verbose_name='In Treatment'),
        ),
        migrations.AlterField(
            model_name='consultationdata',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='consultationdata',
            name='imc_reduction',
            field=models.FloatField(blank=True, null=True, verbose_name='I.M.C. reduction'),
        ),
        migrations.AlterField(
            model_name='consultationdata',
            name='lost_weight',
            field=models.FloatField(blank=True, null=True, verbose_name='Lost Weight'),
        ),
        migrations.AlterField(
            model_name='consultationdata',
            name='pc_reduction',
            field=models.FloatField(blank=True, null=True, verbose_name='P.C. reduction'),
        ),
        migrations.AlterField(
            model_name='consultationdata',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Start Date'),
        ),
        migrations.AlterField(
            model_name='consultationdata',
            name='visit_number',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Visit Number'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='anxiety',
            field=models.NullBooleanField(verbose_name='Anxiety'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='anxiety_treatment',
            field=models.NullBooleanField(verbose_name='Anxiety Treatment'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='aversions',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Aversions'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='children',
            field=models.IntegerField(blank=True, null=True, verbose_name='Children'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='cholesterol',
            field=models.NullBooleanField(verbose_name='Cholesterol'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='cholesterol_total',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Cholesterol Total'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='cholesterol_treatment',
            field=models.NullBooleanField(verbose_name='Cholesterol Treatment'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='constipation',
            field=models.NullBooleanField(verbose_name='Constipation'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='constipation_treatment',
            field=models.NullBooleanField(verbose_name='Constipation Treatment'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='depression',
            field=models.NullBooleanField(verbose_name='Depression'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='depression_treatment',
            field=models.NullBooleanField(verbose_name='Depression Treatment'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='drinks',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Alcohol consumption'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='eats_fast',
            field=models.NullBooleanField(verbose_name='Eats Fast'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='eats_where',
            field=models.CharField(blank=True, choices=[('H', 'At Home'), ('W', 'At Work'), ('S', 'In the Street'), ('F', 'In Family Home'), ('O', 'Other')], max_length=25, null=True, verbose_name='Where has meals'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='eats_with',
            field=models.CharField(blank=True, choices=[('L', 'Alone'), ('I', 'In Company')], max_length=25, null=True, verbose_name='With whom has meals'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='familial_overweight',
            field=models.NullBooleanField(verbose_name='Familial Overweight'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='flatmates',
            field=models.CharField(blank=True, choices=[('L', 'Alone'), ('C', 'With Couple'), ('F', 'With Family')], max_length=25, null=True, verbose_name='Flatmates'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='food_alergies',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Food Alergies'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='hdl',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Cholesterol HDL'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='hta',
            field=models.NullBooleanField(verbose_name='HTA'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='hta_treatment',
            field=models.NullBooleanField(verbose_name='HTA Treatement'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='icm',
            field=models.FloatField(blank=True, null=True, verbose_name='ICM'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='ldl',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Cholesterol LDL'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='n_meals',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Number of daily meals'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='occupation',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Occupation'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='overweight',
            field=models.NullBooleanField(verbose_name='Overweight'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone Number'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='preferences',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Preferences'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sedentarism',
            field=models.NullBooleanField(verbose_name='Sedentarian'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sleep_habits',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Sleep Habits'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sleep_treatment',
            field=models.NullBooleanField(verbose_name='Sleep Treatment'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='smokes',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Number of daily cigarettes'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='snacks',
            field=models.NullBooleanField(verbose_name='Has snacks between meals'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='status',
            field=models.CharField(blank=True, choices=[('M', 'Married'), ('S', 'Single'), ('W', 'Widowed'), ('D', 'Divorced')], max_length=25, null=True, verbose_name='Marital Status'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sugar',
            field=models.NullBooleanField(verbose_name='Sugar'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sugar_level',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Sugar Level'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sugar_treatment',
            field=models.NullBooleanField(verbose_name='Sugar Treatment'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='surgeries',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='History of surgeries'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='tg_level',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Triglycerids Level'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='tg_treatment',
            field=models.NullBooleanField(verbose_name='Triglycerids Treatment'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='thyroid_treatment',
            field=models.NullBooleanField(verbose_name='Thyroid Treatment'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='thyroidism',
            field=models.CharField(blank=True, choices=[('I', 'Hipothyroidims'), ('Y', 'Hyperthyroidims'), ('A', 'Hipo or Hyper'), ('N', 'None')], max_length=25, null=True, verbose_name='Thyroidism'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='triglycerids',
            field=models.NullBooleanField(verbose_name='Triglycerids'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='who_buys',
            field=models.CharField(blank=True, choices=[('P', 'Patient'), ('O', 'Other')], max_length=25, null=True, verbose_name='Who buys food'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='who_cooks',
            field=models.CharField(blank=True, choices=[('P', 'Patient'), ('O', 'Other')], max_length=25, null=True, verbose_name='Who cooks food'),
        ),
    ]