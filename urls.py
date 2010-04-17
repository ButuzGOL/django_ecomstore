from django.conf.urls.defaults import *
from ecomstore import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

import os
static = os.path.join(
                      os.path.dirname(__file__), 'static'
)


urlpatterns = patterns('',
                       (r'^catalog/?', 'preview.views.home'),

    # Example:
    # (r'^ecomstore/', include('ecomstore.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
   urlpatterns += patterns('',
                        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
          { 'document_root' : static }),
)
