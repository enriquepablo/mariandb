from django.db import models
from django.utils.translation import ugettext as _



# XXX placeholders, defaults

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
    ATHOME = 'H'
    WORK = 'W'
    STREET = 'S'
    FAMILY = 'F'
    OTHER = 'O'
    WHERE_CHOICES = (
        (ATHOME, _('At Home')),
        (WORK, _('At Work')),
        (STREET, _('In the Street')),
        (FAMILY, _('In Family Home')),
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

    birthday = models.DateField(verbose_name=_('Birthday'),
                        null=True, blank=True)

    status = models.CharField(max_length=25, verbose_name=_('Marital Status'),
                          choices=MARITAL_STATUS_CHOICES,
                        null=True, blank=True)

    phone = models.CharField(max_length=255, verbose_name=_('Phone Number'),
                        null=True, blank=True)

    email = models.EmailField(verbose_name=_('Email'), null=True, blank=True)

    children = models.IntegerField(verbose_name=_('Children'),
                        null=True, blank=True)

    occupation = models.CharField(max_length=255, verbose_name=_('Occupation'),
                        null=True, blank=True)

    consultation_reason = models.TextField(null=True, blank=True,
                                     verbose_name=_('Reason for consultation'))

    familial_overweight = models.NullBooleanField(
                                        verbose_name=_('Familial Overweight'))

    flatmates = models.CharField(max_length=25, verbose_name=_('Flatmates'),
                          choices=FLATMATE_CHOICES,
                        null=True, blank=True)

    n_meals = models.PositiveSmallIntegerField(
                          verbose_name=_('Number of daily meals'),
                        null=True, blank=True)

    snacks = models.NullBooleanField(verbose_name=_('Has snacks between meals'))

    eats_where = models.CharField(max_length=25,
                verbose_name=_('Where has meals'), choices=WHERE_CHOICES,
                        null=True, blank=True)

    eats_with = models.CharField(max_length=25,
                verbose_name=_('With whom has meals'), choices=WITH_CHOICES,
                        null=True, blank=True)

    eats_fast = models.NullBooleanField(verbose_name=_('Eats Fast'))

    who_buys = models.CharField(max_length=25,
                verbose_name=_('Who buys food'), choices=WHO_CHOICES,
                        null=True, blank=True)

    who_cooks = models.CharField(max_length=25,
                verbose_name=_('Who cooks food'), choices=WHO_CHOICES,
                        null=True, blank=True)

    preferences = models.CharField(max_length=255,
                                verbose_name=_('Preferences'),
                        null=True, blank=True)

    aversions = models.CharField(max_length=255,
                                verbose_name=_('Aversions'),
                        null=True, blank=True)

    overweight =  models.NullBooleanField(verbose_name=_('Overweight'))

    icm =  models.FloatField(verbose_name=_('ICM'),
                        null=True, blank=True)

    smokes = models.PositiveSmallIntegerField(
                          verbose_name=_('Number of daily cigarettes'),
                        null=True, blank=True)

    drinks = models.CharField(max_length=255,
                                verbose_name=_('Alcohol consumption'),
                        null=True, blank=True)

    sedentarism =  models.NullBooleanField(verbose_name=_('Sedentarian'))

    hta =  models.NullBooleanField(verbose_name=_('HTA'))

    hta_treatment = models.NullBooleanField(verbose_name=_('HTA Treatement'))

    cholesterol = models.NullBooleanField(verbose_name=_('Cholesterol'))

    cholesterol_treatment = models.NullBooleanField(
                              verbose_name=_('Cholesterol Treatment'))

    hdl = models.PositiveSmallIntegerField(
                          verbose_name=_('Cholesterol HDL'),
                        null=True, blank=True)

    ldl = models.PositiveSmallIntegerField(
                          verbose_name=_('Cholesterol LDL'),
                        null=True, blank=True)

    cholesterol_total = models.PositiveSmallIntegerField(
                          verbose_name=_('Cholesterol Total'),
                        null=True, blank=True)

    triglycerids = models.NullBooleanField(verbose_name=_('Triglycerids'))

    tg_treatment = models.NullBooleanField(
                              verbose_name=_('Triglycerids Treatment'))

    tg_level = models.PositiveSmallIntegerField(
                          verbose_name=_('Triglycerids Level'),
                        null=True, blank=True)

    sugar = models.NullBooleanField(verbose_name=_('Sugar'))

    sugar_treatment = models.NullBooleanField(
                              verbose_name=_('Sugar Treatment'))

    sugar_level = models.PositiveSmallIntegerField(
                          verbose_name=_('Sugar Level'),
                        null=True, blank=True)

    surgeries = models.CharField(max_length=255,
                                verbose_name=_('History of surgeries'),
                        null=True, blank=True)

    anxiety = models.NullBooleanField(verbose_name=_('Anxiety'))

    anxiety_treatment = models.NullBooleanField(
                              verbose_name=_('Anxiety Treatment'))

    depression = models.NullBooleanField(verbose_name=_('Depression'))

    depression_treatment = models.NullBooleanField(
                              verbose_name=_('Depression Treatment'))

    constipation = models.NullBooleanField(verbose_name=_('Constipation'))

    constipation_treatment = models.NullBooleanField(
                              verbose_name=_('Constipation Treatment'))

    thyroidism = models.CharField(max_length=25,
                verbose_name=_('Thyroidism'), choices=THYROID_CHOICES,
                        null=True, blank=True)

    thyroid_treatment = models.NullBooleanField(
                              verbose_name=_('Thyroid Treatment'))

    food_alergies = models.CharField(max_length=255,
                                verbose_name=_('Food Alergies'),
                        null=True, blank=True)

    sleep_habits = models.CharField(max_length=255,
                                verbose_name=_('Sleep Habits'),
                        null=True, blank=True)

    sleep_treatment = models.NullBooleanField(
                              verbose_name=_('Sleep Treatment'))


class BiochemAnalysis(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,
                     verbose_name=_('Patient'),
                     related_name='biochem_analysis')

    date = models.DateField(verbose_name=_('Date of analysis'),
                        null=True, blank=True)

    hdl = models.PositiveSmallIntegerField(
                          verbose_name=_('Cholesterol HDL'),
                        null=True, blank=True)

    ldl = models.PositiveSmallIntegerField(
                          verbose_name=_('Cholesterol LDL'),
                        null=True, blank=True)

    cholesterol_total = models.PositiveSmallIntegerField(
                          verbose_name=_('Cholesterol Total'),
                        null=True, blank=True)

    tg_level = models.PositiveSmallIntegerField(
                          verbose_name=_('Triglycerids Level'),
                        null=True, blank=True)

    sugar_level = models.PositiveSmallIntegerField(
                          verbose_name=_('Sugar Level'),
                        null=True, blank=True)

    uric_acid = models.FloatField(verbose_name=_('Uric Acid'),
                        null=True, blank=True)

    iron = models.FloatField(verbose_name=_('Iron'),
                        null=True, blank=True)

    calcium = models.FloatField(verbose_name=_('Calcium'),
                        null=True, blank=True)


class BloodPressure(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,
                     verbose_name=_('Patient'),
                     related_name='blood_pressure_report')

    date = models.DateField(verbose_name=_('Date of report'),
                        null=True, blank=True)

    left_arm_high = models.FloatField(verbose_name=_('Left Arm High'),
                        null=True, blank=True)
    left_arm_low = models.FloatField(verbose_name=_('Left Arm Low'),
                        null=True, blank=True)
    right_arm_high = models.FloatField(verbose_name=_('Right Arm High'),
                        null=True, blank=True)
    right_arm_low = models.FloatField(verbose_name=_('Right Arm Low'),
                        null=True, blank=True)
    mean_high = models.FloatField(verbose_name=_('Mean High'),
                        null=True, blank=True)
    mean_low = models.FloatField(verbose_name=_('Mean Low'),
                        null=True, blank=True)

    heart_rate = models.PositiveSmallIntegerField(
                          verbose_name=_('Heart Rate'),
                        null=True, blank=True)

    treatment = models.NullBooleanField(verbose_name=_('In Treatment'))


class ConsultationData(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,
                     verbose_name=_('Patient'),
                     related_name='consultation')

    start_date = models.DateField(verbose_name=_('Start Date'),
                        null=True, blank=True)

    end_date = models.DateField(verbose_name=_('End Date'),
                        null=True, blank=True)

    visit_number = models.PositiveSmallIntegerField(
                          verbose_name=_('Visit Number'),
                        null=True, blank=True)

    lost_weight = models.FloatField(verbose_name=_('Lost Weight'),
                        null=True, blank=True)
    imc_reduction = models.FloatField(verbose_name=_('I.M.C. reduction'),
                        null=True, blank=True)
    pc_reduction = models.FloatField(verbose_name=_('P.C. reduction'),
                        null=True, blank=True)


class AntropometricMeasurement(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,
                     verbose_name=_('Patient'),
                     related_name='measurement')

    date = models.DateField(verbose_name=_('Date of measurement'),
                        null=True, blank=True)

    weight = models.FloatField(verbose_name=_('Weight'),
                        null=True, blank=True)
    imc = models.FloatField(verbose_name=_('I.M.C.'),
                        null=True, blank=True)
    chest = models.FloatField(verbose_name=_('Perim. Chest'),
                        null=True, blank=True)
    min_waist = models.FloatField(verbose_name=_('Perim. Waist Min'),
                        null=True, blank=True)
    hip = models.FloatField(verbose_name=_('Perim. Hips'),
                        null=True, blank=True)
    navel = models.FloatField(verbose_name=_('Perim. Navel'),
                        null=True, blank=True)
    thigh = models.FloatField(verbose_name=_('Perim. Thighs'),
                        null=True, blank=True)
    lost_weight = models.FloatField(verbose_name=_('Lost weight'),
                        null=True, blank=True)
    lost_weight_total = models.FloatField(verbose_name=_('Lost weight total'),
                        null=True, blank=True)
    lost_cm = models.FloatField(verbose_name=_('Lost cm (waist)'),
                        null=True, blank=True)
    lost_cm_total = models.FloatField(verbose_name=_('Lost cm total (waist)'),
                        null=True, blank=True)

