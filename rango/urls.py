from django.conf.urls import patterns, url
from rango import views
from django.conf.urls import include
from django.contrib import admin
from registration.backends.simple.views import RegistrationView

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # url(r'^about/$', views.about, name='about'),
    url(r'^category/(?P<category_name_slug>\w+)$', views.category, name='category'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>\w+)/add_page/$', views.add_page, name='add_page'),
    url(r'^category/(?P<category_name_slug>\w+)/viewed_documents/$', views.viewed_documents, name='viewed_documents'),
    url(r'^category/(?P<category_name_slug>\w+)/final/$', views.final, name='final'),
    url(r'^category/(?P<category_name_slug>\w+)/done/$', views.done, name='done'),
    # url(r'^register/$', views.register, name='register'),
    # url(r'^login/$', views.user_login, name='login'),
    url(r'^restricted/', views.restricted, name='restricted'),
    # url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
)

