from django.conf.urls import patterns, url
from sysrev import views

urlpatterns = patterns('',

    # Basic routes
    url(r'^$',          views.index,       name='index'),
    url(r'^about/$',    views.about,       name='about'),
    url(r'^register/$', views.register,    name='register'),
    url(r'^login/$',    views.user_login,  name='login'),
    url(r'^logout/$',   views.user_logout, name='logout'),

    # SysRev routes
    url(r'^dashboard/$',        views.dashboard,     name='dashboard'),
    url(r'^add_review/$',       views.add_review,    name='add_review'),
    url(r'^review/(\d+)/$',     views.review,        name='review'),
    url(r'^delete/(\d+)/$',     views.delete_review, name='delete_review'),
    url(r'^get_doc_count/$',    views.get_doc_count, name='get_doc_count'),
    url(r'^review/abstract/(\d+)/(\d+)/$', views.mark_abstract, name='mark_abstract'),
    url(r'^review/document/(\d+)/(\d+)/$', views.mark_document, name='mark_document'),
    url(r'^review/edit/(\d+)/$',           views.edit_review,   name='edit_review'),
    url(r'^review/done/(\d+)/(\S+)/$',     views.end_stage,     name='end_stage'),

    # Update profile routes
    url(r'^update_profile/$',  views.update_profile,  name='update_profile'),
    url(r'^update_password/$', views.update_password, name='update_password'),
    url(r'^update_email/$',    views.update_email,    name='update_email'),

)

