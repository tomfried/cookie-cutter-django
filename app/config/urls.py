from django.contrib import admin
from django.urls import path, include
from backend.controllers import about, errors, example_form, home, style_guide

handler400 = errors.error_400
handler403 = errors.error_403
handler404 = errors.error_404
handler500 = errors.error_500

urlpatterns = [
    path('', home.index, name='home'),
    path('about/', about.index, name='about'),
    path('example_form/', example_form.index, name='example_form'),
    path('style_guide/', style_guide.index, name='style_guide'),
]
