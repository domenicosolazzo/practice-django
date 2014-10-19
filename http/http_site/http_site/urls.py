from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'http_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^articles/2003/$', views.special_case_2003),
    url(r'^articles/(?P<year>\d{4})/$', views.year_archive),

    #A request to /articles/2005/03/ would call
    #the function views.month_archive(request, year='2005', month='03'),
    #instead of views.month_archive(request, '2005', '03').
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/$', views.month_archive),
    # A request to /articles/2003/03/03/ would call
    # the function views.article_detail(request, year='2003', month='03', day='03')
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/$', views.article_detail),
    # Defaults for view arguments
    url(r'^blog/page(?P<num>\d+)/$', views.page),
    url(r'^admin/', include(admin.site.urls))
)
