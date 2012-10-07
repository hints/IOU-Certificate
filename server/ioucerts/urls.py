from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'redeem.views.home', name='home'),
    url(r'^create_user/', 'redeem.views.create_user'),
    url(r'^sync/', 'redeem.views.sync'),
    url(r'^redeemed/$', 'redeem.views.redeemed'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<redeem_code>.+)/$', 'redeem.views.redeem'),
    # url(r'^ioucerts/', include('ioucerts.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
)
