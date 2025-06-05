from django.shortcuts import render
from .common import get_base_page_information

def index(request):

    context = {
        # The breadcrumbs, body_classes, and browser_title
        'base': get_base_page_information(request, 'About'),
    }
    return render(request, 'about/index.html', context)
