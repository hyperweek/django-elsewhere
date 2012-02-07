from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('elsewhere.views',
    url(r'^$', 'elsewhere', name='elsewhere'),
)
