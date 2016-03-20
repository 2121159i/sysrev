from django.conf.urls import patterns, url
from sysrev import views
from django.conf.urls import include
from django.contrib import admin
from registration.backends.simple.views import RegistrationView

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),

    #Old URLS Category
    #url(r'^category/(?P<category_name_slug>\w+)$', views.category, name='category'),
    url(r'^category/(?P<category_name_slug>\w+)/add_page/$', views.add_page, name='add_page'),
    url(r'^category/(?P<category_name_slug>\w+)/viewed_documents/$', views.viewed_documents, name='viewed_documents'),
    url(r'^category/(?P<category_name_slug>\w+)/final/$', views.final, name='final'),
    url(r'^category/(?P<category_name_slug>\w+)/done/$', views.done, name='done'),
    ##

    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),


    #New URLS Review
    url(r'^review/(\d+)/$',views.review,name='review'),

    # Dom's routes
    url(r'^dashboard/$',        views.dashboard,     name='dashboard'),
    url(r'^add_category/$',     views.add_category,  name='add_category'),
    url(r'^delete/(\d+)/$',     views.delete_review, name='delete_review'),
    url(r'^get_doc_count/$',    views.get_doc_count, name='get_doc_count'),
    url(r'^review/abstract/(\d+)/(\d+)/$',views.mark_abstract, name='mark_abstract'),
    url(r'^review/document/(\d+)/(\d+)/$',views.mark_document, name='mark_document'),

    # Update profile urls
    url(r'^update_profile/$', views.update_profile, name='update_profile'),
    url(r'^update_password/$', views.update_password, name='update_password'),
    url(r'^update_email/$', views.update_email, name='update_email'),

    # url(r'^register/$', views.register, name='register'),
    # url(r'^login/$', views.user_login, name='login'),
    # url(r'^restricted/', views.restricted, name='restricted'),
    # url(r'^logout/$', views.user_logout, name='logout'),
	# url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
)

