from django.contrib import admin
from django.contrib.auth.models import Group
from .models import BarreRaccourcie, Projet, Vekflix, UploadPassword,Exercice
from django.urls import path
from django.http import HttpResponseRedirect
from django.utils.html import format_html


admin.site.site_header = 'Veksor Hub Administration'


class BarreAdmin(admin.ModelAdmin):
    list_display = ('title','url')


class UploadPasswordAdmin(admin.ModelAdmin):
    list_display = ('password',)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','created','font_size_html_display','language','url',)
    list_filter = ('created','language')
    change_list_template = 'admin/projects/projects_change_list.html'
    ordering = ['title']


    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('fontsize/<int:size>/', self.change_font_size)
        ]
        return custom_urls + urls

    def change_font_size(self, request, size):
        self.model.objects.all().update(font_size=size)
        self.message_user(request, 'Font size set successfully !')
        return HttpResponseRedirect("../")

    def font_size_html_display(self, obj):
        display_size = obj.font_size if obj.font_size <= 50 else 30
        return format_html(
            f'<span style="font-size: {display_size}px;">{obj.font_size}</span>'
        )


class VekflixAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ()

class ExerciceAdmin(admin.ModelAdmin):
    list_display = ('annee','chapitres','points')
    list_filter = ()

admin.site.register(BarreRaccourcie, BarreAdmin)
admin.site.register(UploadPassword, UploadPasswordAdmin)
admin.site.register(Projet, ProjectAdmin)
admin.site.register(Vekflix, VekflixAdmin)
admin.site.register(Exercice, ExerciceAdmin)
admin.site.unregister(Group)
# Register your models here.
