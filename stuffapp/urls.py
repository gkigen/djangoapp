from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'stuffapp.views.list_stuff', name="list-stuff"),
    url(r'^(?P<thing_id>\d+)/$', 'stuffapp.views.thing_detail', 
        name='thing-detail'),
    url(r'^create/$', 'stuffapp.views.create_stuff',
        name="create-stuff"),
    url(r'^edit/(?P<thing_id>\d+)/$', 'stuffapp.views.edit_stuff',
        name='edit-stuff'),
    url(r'^delete/(?P<thing_id>\d+)/$', 'stuffapp.views.delete_stuff',
        name='delete-stuff'), 
)        