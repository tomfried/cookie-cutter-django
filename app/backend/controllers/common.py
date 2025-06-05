from datetime import date
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from http import HTTPStatus
from pathlib import Path
import os, datetime, logging, traceback


def get_base_page_information(request, page_title):
    # Check if using supported browser
    if is_unsupported_browser(request):
        return error_unsupport_browser(request)

    if request.user.is_authenticated:
        signed_in = True
    else:
        signed_in = False

    # ===== Feature Flags ===== #
    feature_flags = {
        # These are just examples of best practice of handling feature flags.
        ## In HTML would use base.feature_flags.SOCIALACCOUNT_QUERY_EMAIL to handle something rendering/behaving or not.
        'SOCIALACCOUNT_QUERY_EMAIL': settings.SOCIALACCOUNT_QUERY_EMAIL,
        'ACCOUNT_LOGOUT_ON_GET': settings.ACCOUNT_LOGOUT_ON_GET,
        'ACCOUNT_UNIQUE_EMAIL': settings.ACCOUNT_UNIQUE_EMAIL,
        'ACCOUNT_EMAIL_REQUIRED': settings.ACCOUNT_EMAIL_REQUIRED,
        'SOCIALACCOUNT_ONLY': settings.SOCIALACCOUNT_ONLY,
        'PASSKEY_SIGNUP_ENABLED': settings.PASSKEY_SIGNUP_ENABLED,
        'SOCIALACCOUNT_ENABLED': settings.SOCIALACCOUNT_ENABLED,
    }

    base_context = {
        'body_classes': setup_body_classes(request, page_title),
        'breadcrumbs': generate_breadcrumbs(request),
        'browser_title': page_title,
        'signed_in': signed_in,
        'feature_flags': feature_flags,
    }
    return base_context

####################################
####### Generate Breadcrumbs #######
####################################
def generate_breadcrumbs(request):
    breadcrumbs = [{'name': 'Home', 'url': '/'}]
    path = request.META.get('PATH_INFO').split('/')
    path = [directory for directory in path if directory != ""]
    for index, directory in enumerate(path):
        breadcrumbs.append({'name': directory.replace('_',' ').title(), 'url': breadcrumbs[index].get('url') + directory + '/' })
    breadcrumbs.pop(0)
    return breadcrumbs

####################################
########### Body Classes ###########
####################################
def setup_body_classes(request, page_title):
    # Page body class
    body_classes = 'page-' + page_title.replace(' ', '-').lower() + ' '
    path = request.META.get('PATH_INFO').split('/')[1:]
    print("Path:" + str(path))
    if len(path[0]) > 1:
        body_classes += 'directory-' + path[0].replace(' ', '-').lower() + ' '

    # Browser & Platform
    try:
        if request.user_agent.browser.family == 'Chrome':
            body_classes += 'browser-chrome browser-chrome-' + request.user_agent.browser.version_string.split('.', 1)[0] + ' '
        elif request.user_agent.browser.family == 'Firefox':
            body_classes += 'browser-firefox browser-firefox-' + request.user_agent.browser.version_string.split('.', 1)[0] + ' '
        elif request.user_agent.browser.family.lower() == 'msie':
            body_classes += 'browser-internet-explorer browser-internet-explorer-' + request.user_agent.browser.version_string.split('.', 1)[0] + ' '
        elif request.user_agent.browser.family == 'Edge':
            body_classes += 'browser-edge browser-edge-' + request.user_agent.browser.version_string.split('.', 1)[0] + ' '
        else:
            body_classes += 'browser-unknown browser-unknown-' + request.user_agent.browser.version_string.split('.', 1)[0] + ' '

        ## Platforms
        body_classes += 'platform-' + request.user_agent.os.family.replace(' ', '-').lower() + ' '
        if request.user_agent.os.version_string != '':
            body_classes += 'platform-' + request.user_agent.os.family.replace(' ', '-').lower() + '-' + request.user_agent.os.version_string.split('.', 1)[0] + ' '
    except Exception as e:
        body_classes += 'browser-unknown platform-unknown'

    if request.user.is_authenticated:
        body_classes += 'user-authenticated'
    else:
        body_classes += 'user-anonymous'

    return body_classes

#####################################
##### Unsupported Browser Check #####
#####################################
def is_unsupported_browser(request):
    try:
        # All versions of Internet Explorer are unsupported
        if request.user_agent.browser.family.lower() == 'msie' or request.user_agent.browser.version_string.split('.', 1)[0] == '11':
            return True
    except Exception as e:
        return False
    return False
