from django.conf.urls import url
from . import views


urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /product/
    url(r'^product$', views.product_list, name='product_list'),
    # ex: /product/5/
    url(r'^product/(?P<product_id>[0-9]+)/$', views.product_detail, name='product_detail'),
    url(r'^product/(?P<product_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
]