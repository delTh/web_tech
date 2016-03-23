from django.conf.urls import patterns, include, url

from django.contrib import admin
from qa import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^question/(?P<qid>\d+)/$', views.question),
	url(r'^$', views.mainpage),
	url(r'^login/.*$', views.test),
	url(r'^signup/.*$', views.test),
	url(r'^ask/.*$', views.test),
	url(r'^popular/.*$', views.popular),
	url(r'^new/.*$', views.test)
)
