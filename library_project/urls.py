from django.conf.urls import include, url

from django.contrib import admin
from django.contrib.auth import views as auth_views
# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^', include('home.urls', namespace='home')),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^donations/', include('donations.urls', namespace='donations')),
    url(r'^transactions/', include('transactions.urls', name='transactions')),
    url(r'^admin/', include(admin.site.urls)),
]
