from django.contrib import admin
from .models import *


@admin.register(CurriculumVitae)
class CurriculumVitaeAdmin(admin.ModelAdmin):
    ...

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "author",
    )

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "company",
        "position",
    )

@admin.register(ProgrammingLanguage)
class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "college",
    )

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("name",)
