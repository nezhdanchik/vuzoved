from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import University, Feedback, User

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('short_body', 'rate', 'time_created', 'university', 'user')
    list_editable = ('rate',)

    def short_body(self, feedback):
        return f"{feedback.body[:50]}..."


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'short_description')
    list_filter = ('rating', )

    def short_description(self, university):
        return f"{university.description[:50]}..."


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'points')
    list_editable = ('role',)