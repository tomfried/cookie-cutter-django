import os

if os.environ['DJANGO_APP'] == 'prod' and 'DJANGO_APP_IN_CONTAINER' in os.environ:
    bind = '0.0.0.0:8000'
else:
    bind = '127.0.0.1:3000'
    keyfile = '/etc/pki/nginx/server.key'
    certfile = '/etc/pki/nginx/server.crt'
    #ca_certs = '/etc/pki/jks/allTrustedPartnersKS.jks'
    secure_scheme_headers = {'X-FORWARDED_PROTOCOL':'ssl', 'X-FORWARDED-PROTO':'https', 'X-FORWARDED-SSL':'on'}
