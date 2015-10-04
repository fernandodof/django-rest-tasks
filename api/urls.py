from django.conf.urls import patterns, url

urlpatterns = patterns(
    'api.views',
    #url(r'^person/$', 'person_list', name='person_list'),
 	#url(r'^person-paginated/(?:(?P<search>[a-zA-Z]+)/)?(?:(?P<order>[a-zA-Z]+)/)?$', 'person_list_paginated', name='person_list_paginated'),
    url(r'^person/(?P<pk>[0-9]+)$', 'person', name='person'),
    url(r'^person/(?:(?P<search>[a-zA-Z]+)/)?(?:(?P<order>[a-zA-Z]+)/)?$', 'person', name='person'),
)