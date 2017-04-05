from django.conf.urls import include, url

from django.contrib import admin

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^', include('home.urls', namespace='home')),
    url(r'^donations/', include('donations.urls', namespace='donations')),
    url(r'^admin/', include(admin.site.urls)),
]
