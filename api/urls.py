from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.views',
    url(r'^person/$', 'person_list', name='person_list'),
 	url(r'^person-paginated/$', 'person_list_paginated', name='person_list_paginated'),
    url(r'^persons/(?P<pk>[0-9]+)$', 'person_detail', name='person_detail'),
)