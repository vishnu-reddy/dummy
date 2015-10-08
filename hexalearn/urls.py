from django.conf.urls import include, url
from django.views.static import *
from django.contrib import admin
from sample import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'hexalearn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.employee_register),
]
