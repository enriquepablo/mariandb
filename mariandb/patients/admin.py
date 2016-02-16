from django.contrib import admin
from django.utils.translation import ugettext as _

from .models import Patient, BiochemAnalysis
from .models import BloodPressure, ConsultationData, AntropometricMeasurement


class AnalysisInline(admin.StackedInline):
    model = BloodPressure
    verbose_name = _('Blood Presure Report')
    verbose_name_plural = _('Blood Presure Reports')
    ordering = ('date',)
    min_num = 1


class BloodInline(admin.StackedInline):
    model = BiochemAnalysis
    verbose_name = _('Biochemocal Analysis')
    verbose_name_plural = _('Biochemocal Analysis')
    ordering = ('date',)
    min_num = 1


class ConsultationInline(admin.StackedInline):
    model = ConsultationData
    verbose_name = _('Consultation Data Set')
    verbose_name_plural = _('Consultation Data Sets')
    ordering = ('start_date',)
    min_num = 1


class MeasurementInline(admin.StackedInline):
    model = AntropometricMeasurement
    verbose_name = _('Antropometric Measurement')
    verbose_name_plural = _('Antropometric Measurements')
    ordering = ('date',)
    min_num = 1


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    inlines = [AnalysisInline, BloodInline, ConsultationInline,
                MeasurementInline]
    list_display = ('name', 'surname', 'phone', 'birthday')
    list_filter = ('sex', 'birthday', 'status', 'children',
                'familial_overweight', 'flatmates', 'n_meals')
    search_fields = ('name', 'surname',  'status',  'occupation',
                'consultation_reason')


@admin.register(BiochemAnalysis)
class AnalysisAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date', 'cholesterol_total', 'sugar_level',
              'tg_level', 'uric_acid', 'iron', 'calcium')
    list_filter = ('patient',)


@admin.register(BloodPressure)
class BloodAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date', 'mean_high', 'mean_low',
                    'heart_rate', 'treatment')
    list_filter = ('patient',)


@admin.register(ConsultationData)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'start_date', 'end_date', 'visit_number',
                    'lost_weight')
    list_filter = ('patient',)


@admin.register(AntropometricMeasurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date', 'weight', 'lost_weight',
                    'lost_weight_total')
    list_filter = ('patient',)

