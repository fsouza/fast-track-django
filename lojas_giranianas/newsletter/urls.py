from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^cadastrar', 'newsletter.views.cadastrar_newsletter', name='cadastrar_newsletter'),
)
