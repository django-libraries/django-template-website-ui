from django.shortcuts import render, redirect


# Website
def index(request):
    return render(request, 'website/index.html')


def about_us(request):
    return render(request, 'website/about-us.html')


def contact_us(request):
    return render(request, 'website/contact-us.html')


def author(request):
    return render(request, 'website/author.html')


# Sections
def presentation(request):
    return render(request, 'website/sections/presentation.html')


def page_header(request):
    return render(request, 'website/sections/page-sections/hero-sections.html')


def features(request):
    return render(request, 'website/sections/page-sections/features.html')


def navbars(request):
    return render(request, 'website/sections/navigation/navbars.html')


def nav_tabs(request):
    return render(request, 'website/sections/navigation/nav-tabs.html')


def pagination(request):
    return render(request, 'website/sections/navigation/pagination.html')


def inputs(request):
    return render(request, 'website/sections/input-areas/inputs.html')


def forms(request):
    return render(request, 'website/sections/input-areas/forms.html')


def avatars(request):
    return render(request, 'website/sections/elements/avatars.html')


def badges(request):
    return render(request, 'website/sections/elements/badges.html')


def breadcrumbs(request):
    return render(request, 'website/sections/elements/breadcrumbs.html')


def buttons(request):
    return render(request, 'website/sections/elements/buttons.html')


def dropdowns(request):
    return render(request, 'website/sections/elements/dropdowns.html')


def progress_bars(request):
    return render(request, 'website/sections/elements/progress-bars.html')


def toggles(request):
    return render(request, 'website/sections/elements/toggles.html')


def typography(request):
    return render(request, 'website/sections/elements/typography.html')


def alerts(request):
    return render(request, 'website/sections/attention-catchers/alerts.html')


def modals(request):
    return render(request, 'website/sections/attention-catchers/modals.html')


def tooltips(request):
    return render(request, 'website/sections/attention-catchers/tooltips-popovers.html')
