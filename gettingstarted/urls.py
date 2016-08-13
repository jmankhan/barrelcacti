from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import barrelcacti.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', barrelcacti.views.index),
    url(r'^db', barrelcacti.views.db),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
]
