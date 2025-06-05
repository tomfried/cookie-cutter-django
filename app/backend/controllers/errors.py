from django.shortcuts import render
from .common import get_base_page_information

def error_400(request, *args, **argv):
    #context = get_context(request, *args)
    #print_clean_error_to_console(request, 'ERROR 400. Request: {}\n{}'.format(request, context['console_message']))
    context = {
        # The breadcrumbs, body_classes, and browser_title
        'base': get_base_page_information(request, 'Error 400'),
    }
    return render(request, 'errors/400.html', context, status='400')

def error_403(request, *args, **argv):
    #context = get_context(request, *args)
    #print_clean_error_to_console(request, 'ERROR 403. Request: {}\n{}'.format(request, context['console_message']))
    context = {
        # The breadcrumbs, body_classes, and browser_title
        'base': get_base_page_information(request, 'Error 403'),
    }
    return render(request, 'errors/403.html', context, status='403')

def error_404(request, *args, **argv):
    #context = get_context(request, *args)
    #print_clean_error_to_console(request, 'ERROR 404. Request: {}\n{}'.format(request, context['console_message']))
    context = {
        # The breadcrumbs, body_classes, and browser_title
        'base': get_base_page_information(request, 'Error 404'),
    }
    return render(request, 'errors/404.html', context, status='404')

def error_500(request, *args, **argv):
    #context = get_context(request, *args)
    #print_clean_error_to_console(request, 'ERROR 500. Request: {}\n{}'.format(request, *args))
    context = {
        # The breadcrumbs, body_classes, and browser_title
        'base': get_base_page_information(request, 'Error 500'),
    }
    return render(request, 'errors/500.html', context, status='500')

def error_unsupport_browser(request):
    #message = 'You are using an unsupported internet browser (Internet Explorer). Please use either Chrome or Edge. IE is not only unsecure but it does not support.'
    #message = 'Unsupported browser'
    #print_clean_error_to_console(request, 'BROWSER ERROR. Request: {}\n{}'.format(request, context['console_message']))
    context = {
        # The breadcrumbs, body_classes, and browser_title
        'base': get_base_page_information(request, 'Error Unsupported Browser'),
    }
    return render(request, 'errors/unsupported_browser.html', context, status='403')
