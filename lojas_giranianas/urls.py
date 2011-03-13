from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^media/(.*)', 'django.views.static.serve', { 'document_root' : settings.MEDIA_ROOT }),
    (r'^armazem/', include('armazem.urls', app_name='armazem', namespace='armazem')),
    (r'^newsletter/', include('newsletter.urls', app_name='newsletter', namespace='newsletter')),
    (r'^fotos/', include('galeria.urls', app_name='galeria', namespace='galeria')),
    url(r'^contato/', 'contato.views.contato', name='contato'),
    url(r'^$', 'django.views.generic.simple.direct_to_template', { 'template' : 'home.html' }, name='home'),
)
