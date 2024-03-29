from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from registration.forms import RegistrationFormUniqueEmail
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name="core/index.html"), name='home'),
    url(r'^test/$', TemplateView.as_view(template_name="core/test.html"), name='test'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$',
        "registration.views.register",
        {'backend': 'registration.backends.default.DefaultBackend', 'form_class' : RegistrationFormUniqueEmail},
        name='registration_register'), 
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r"^profiles/", include("easy_profiles.urls")),

)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL, 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
        )
