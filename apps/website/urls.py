from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('about-us/', views.about_us, name='about-us'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('author/', views.author, name='author'),

    # Sections
    path('presentation/', views.presentation, name='presentation'),
    path('page-header/', views.page_header, name='page_header'),
    path('features/', views.features, name='features'),
    path('navbars/', views.navbars, name='navbars'),
    path('nav-tabs/', views.nav_tabs, name='nav_tabs'),
    path('pagination/', views.pagination, name='pagination'),
    path('inputs/', views.inputs, name='inputs'),
    path('forms/', views.forms, name='forms'),
    path('alerts/', views.alerts, name='alerts'),
    path('modals/', views.modals, name='modals'),
    path('tooltips/', views.tooltips, name='tooltips'),
    path('avatars/', views.avatars, name='avatars'),
    path('badges/', views.badges, name='badges'),
    path('breadcrumbs/', views.breadcrumbs, name='breadcrumbs'),
    path('buttons/', views.buttons, name='buttons'),
    path('dropdowns/', views.dropdowns, name='dropdowns'),
    path('progress-bars/', views.progress_bars, name='progress_bars'),
    path('toggles/', views.toggles, name='toggles'),
    path('typography/', views.typography, name='typography'),
]
