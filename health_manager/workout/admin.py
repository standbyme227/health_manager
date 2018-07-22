from django.contrib import admin

# Register your models here.
from workout.models import *


class WorkoutPackageAdmin(admin.ModelAdmin):
    list_display = []
    list_filter = []
    search_fields = []
    filter_horizontal = []

class WorkoutSetAdmin(admin.ModelAdmin):
    list_display = []
    list_filter = []
    search_fields = []
    filter_horizontal = []

class RoutineAdmin(admin.ModelAdmin):
    list_display = []
    list_filter = []
    search_fields = []
    filter_horizontal = []

class WorkoutDetailAdmin(admin.ModelAdmin):
    list_display = []
    list_filter = []
    search_fields = []
    filter_horizontal = []

class RoutineToWorkoutSetAdmin(admin.ModelAdmin):
    list_display = []
    list_filter = []
    search_fields = []
    filter_horizontal = []





admin.site.register(WorkoutPackage, WorkoutPackageAdmin)
admin.site.register(WorkoutSet, WorkoutSetAdmin)
admin.site.register(WorkoutDetail, WorkoutDetailAdmin)
admin.site.register(Routine, RoutineAdmin)
admin.site.register(RoutineToWorkoutSet, RoutineToWorkoutSetAdmin)
