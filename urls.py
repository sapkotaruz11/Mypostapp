from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'postreply.views.home', name='home'),
    url(r'^add/$', 'postreply.views.addpost', name="addpost"),
    url(r'^getdata/$', 'postreply.views.getdata', name="getdata"),
    url(r'^home/$', 'postreply.views.postform', name="homepage"),
    url(r'^reply/$', 'postreply.views.addreply', name="addreply"),


)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
