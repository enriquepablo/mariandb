from django.db import models
from django.utils.translation import ugettext as _


class Patient(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = (
        (MALE, _('Male')),
        (FEMALE, _('Female')))
    MARRIED = 'M'
    SINGLE = 'S'
    WIDOWED = 'W'
    DIVORCED = 'D'
    MARITAL_STATUS_CHOICES = (
        (MARRIED, _('Married')),
        (SINGLE, _('Single')),
        (WIDOWED, _('Widowed')),
        (DIVORCED, _('Divorced')))
    LONE = 'L'
    COUPLE = 'C'
    FAMILY = 'F'
    FLATMATE_CHOICES = (
        (LONE, _('Alone')),
        (COUPLE, _('With Couple')),
        (FAMILY, _('With Family')))
    HOME = 'H'
    WORK = 'W'
    STREET = 'S'
    FAMILY = 'F'
    OTHER = 'O'
    WHERE_CHOICES = (
        (HOME, _('Home')),
        (WORK, _('Work')),
        (STREET, _('Street')),
        (FAMILY, _('Family')),
        (OTHER, _('Other')))
    INCOMPANY = 'I'
    WITH_CHOICES = (
        (LONE, _('Alone')),
        (INCOMPANY, _('In Company')))
    PATIENT = 'P'
    WHO_CHOICES = (
        (PATIENT, _('Patient')),
        (OTHER, _('Other')))
    HIPO = 'I'
    HYPER = 'Y'
    ANY = 'A'
    NONE = 'N'
    THYROID_CHOICES = (
        (HIPO, _('Hipothyroidims')),
        (HYPER, _('Hyperthyroidims')),
        (ANY, _('Hipo or Hyper')),
        (NONE, _('None')))


    name = models.CharField(max_length=255, verbose_name=_('First Name'))

    surname = models.CharField(max_length=255, verbose_name=_('Last Name'))

    sex = models.CharField(max_length=25, verbose_name=_('Sex'),
                          choices=SEX_CHOICES)

    birthday = models.DateField(verbose_name=_('Birthday'))

    status = models.CharField(max_length=25, verbose_name=_('Marital Status'),
                          choices=MARITAL_STATUS_CHOICES)

    phone = models.CharField(max_length=255, verbose_name=_('Phone Number'))

    email = models.EmailField(verbose_name=_('Email'), null=True, blank=True)

    children = models.IntegerField(verbose_name=_('Children'))

    occupation = models.CharField(max_length=255, verbose_name=_('Occupation'))

    consultation_reason = models.TextField(null=True, blank=True,
                                     verbose_name=_('Reason for consultation'))

    familial_overweight = models.BooleanField(
                                        verbose_name=_('Familial Overweight'))

    flatmates = models.CharField(max_length=25, verbose_name=_('Flatmates'),
                          choices=FLATMATE_CHOICES)

    n_meals = models.PositiveSmallIntegerField(
                          verbose_name=_('Number of daily meals'))

    snacks = models.BooleanField(verbose_name=_('Has snacks between meals'))

    eats_where = models.CharField(max_length=25,
                verbose_name=_('Where has meals'), choices=WHERE_CHOICES)

    eats_with = models.CharField(max_length=25,
                verbose_name=_('With whom has meals'), choices=WITH_CHOICES)

    eats_fast = models.BooleanField(verbose_name=_('Eats Fast'))

    who_buys = models.CharField(max_length=25,
                verbose_name=_('Who buys food'), choices=WHO_CHOICES)

    who_cooks = models.CharField(max_length=25,
                verbose_name=_('Who cooks food'), choices=WHO_CHOICES)

    preferences = models.CharField(max_length=255,
                                verbose_name=_('Preferences'))

    aversions = models.CharField(max_length=255,
                                verbose_name=_('Aversions'))

    overweight =  models.BooleanField(verbose_name=_('Overweight'))

    icm =  models.FloatField(verbose_name=_('ICM'))

    smokes = models.PositiveSmallIntegerField(
                          verbose_name=_('Number of daily cigarettes'))

    drinks = models.CharField(max_length=255,
                                verbose_name=_('Alcohol consumption'))

    sedentarism =  models.BooleanField(verbose_name=_('Sedentarian'))

    hta =  models.BooleanField(verbose_name=_('HTA'))

    hta_treatment = models.BooleanField(verbose_name=_('HTA Treatement'))

    cholesterol = models.BooleanField(verbose_name=_('Cholesterol'))

    cholesterol_treatment = models.BooleanField(
                              verbose_name=_('Cholesterol Treatment'))

    hdl = models.PositiveSmallIntegerField(
                          verbose_name=_('Cholesterol HDL'))

    ldl = models.PositiveSmallIntegerField(
                          verbose_name=_('Cholesterol LDL'))

    cholesterol_total = models.PositiveSmallIntegerField(
                          verbose_name=_('Cholesterol Total'))

    triglycerids = models.BooleanField(verbose_name=_('Triglycerids'))

    tg_treatment = models.BooleanField(
                              verbose_name=_('Triglycerids Treatment'))

    tg_level = models.PositiveSmallIntegerField(
                          verbose_name=_('Triglycerids Level'))

    sugar = models.BooleanField(verbose_name=_('Sugar'))

    sugar_treatment = models.BooleanField(
                              verbose_name=_('Sugar Treatment'))

    sugar_level = models.PositiveSmallIntegerField(
                          verbose_name=_('Sugar Level'))

    surgeries = models.CharField(max_length=255,
                                verbose_name=_('History of surgeries'))

    anxiety = models.BooleanField(verbose_name=_('Anxiety'))

    anxiety_treatment = models.BooleanField(
                              verbose_name=_('Anxiety Treatment'))

    depression = models.BooleanField(verbose_name=_('Depression'))

    depression_treatment = models.BooleanField(
                              verbose_name=_('Depression Treatment'))

    constipation = models.BooleanField(verbose_name=_('Constipation'))

    constipation_treatment = models.BooleanField(
                              verbose_name=_('Constipation Treatment'))

    thyroidism = models.CharField(max_length=25,
                verbose_name=_('Thyroidism'), choices=THYROID_CHOICES)

    thyroid_treatment = models.BooleanField(
                              verbose_name=_('Thyroid Treatment'))

    food_alergies = models.CharField(max_length=255,
                                verbose_name=_('Food Alergies'))

    sleep_habits = models.CharField(max_length=255,
                                verbose_name=_('Sleep Habits'))

    sleep_treatment = models.BooleanField(
                              verbose_name=_('Sleep Treatment'))


class BiochemAnalysis(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,
                     verbose_name=_('Patient'),
                     related_name='biochem_analysis')

    date = models.DateField(verbose_name=_('Date of analysis'))

    hdl = models.PositiveSmallIntegerField(
                          verbose_name=_('Cholesterol HDL'))

    ldl = models.PositiveSmallIntegerField(
                          verbose_name=_('Cholesterol LDL'))

    cholesterol_total = models.PositiveSmallIntegerField(
                          verbose_name=_('Cholesterol Total'))

    tg_level = models.PositiveSmallIntegerField(
                          verbose_name=_('Triglycerids Level'))

    sugar_level = models.PositiveSmallIntegerField(
                          verbose_name=_('Sugar Level'))

    uric_acid = models.FloatField(verbose_name=_('Uric Acid'))

    iron = models.FloatField(verbose_name=_('Iron'))

    calcium = models.FloatField(verbose_name=_('Calcium'))


class BloodPressure(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,
                     verbose_name=_('Patient'),
                     related_name='blood_pressure_report')

    date = models.DateField(verbose_name=_('Date of report'))

    left_arm_high = models.FloatField(verbose_name=_('Left Arm High'))
    left_arm_low = models.FloatField(verbose_name=_('Left Arm Low'))
    right_arm_high = models.FloatField(verbose_name=_('Right Arm High'))
    right_arm_low = models.FloatField(verbose_name=_('Right Arm Low'))
    mean_high = models.FloatField(verbose_name=_('Mean High'))
    mean_low = models.FloatField(verbose_name=_('Mean Low'))

    heart_rate = models.PositiveSmallIntegerField(
                          verbose_name=_('Heart Rate'))

    treatment = models.BooleanField(verbose_name=_('In Treatment'))
