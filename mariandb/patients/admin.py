from django.contrib import admin
from .models import Patient, BiochemAnalysis


class AnalysisInline(admin.StackedInline):
    model = BiochemAnalysis


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    inlines = [AnalysisInline]
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

