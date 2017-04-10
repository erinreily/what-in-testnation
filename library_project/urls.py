from django.conf.urls import include, url

from django.contrib import admin
from django.contrib.auth import views as auth_views
# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^', include('home.urls', namespace='home')),
    url(r'^login/$', auth_views.login, name='login'),
<<<<<<< HEAD
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^donations/', include('donations.urls', namespace='donations')),
    url(r'^transactions/', include('transactions.urls')),
    url(r'^member/', include('member.urls', namespace='member')),
    url(r'^staff/', include('staff.urls', namespace='staff')),
    url(r'^meetstaff/', include('meetstaff.urls')),
=======
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^donations/', include('donations.urls', namespace='donations')),
    url(r'^transactions/', include('transactions.urls', namespace='transactions')),
>>>>>>> 1506909a0a168091856c108e091a09dbc075cc7b
    url(r'^admin/', include(admin.site.urls)),
]
