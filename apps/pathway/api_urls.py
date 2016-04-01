# Created by wiggins@concentricsky.com on 3/30/16.
from django.conf.urls import url

from pathway.api import PathwayList, PathwayDetail, PathwayElementDetail, PathwayElementList

urlpatterns = [

    url(r'^$', PathwayList.as_view(), name='pathway_list'),
    url(r'^/(?P<pathway_slug>[^/]+)$', PathwayDetail.as_view(), name='pathway_detail'),
    url(r'^/(?P<pathway_slug>[^/]+)/elements$', PathwayElementList.as_view(), name='pathway_element_list'),
    url(r'^/(?P<pathway_slug>[^/]+)/elements/(?P<element_slug>[^/]+)$', PathwayElementDetail.as_view(), name='pathway_element_detail'),

]
