from django.shortcuts import render
from .common import get_base_page_information

def index(request):

    context = {
        # The breadcrumbs, body_classes, and browser_title
        'base': get_base_page_information(request, 'Home'),
    }
    return render(request, 'home/index.html', context)
